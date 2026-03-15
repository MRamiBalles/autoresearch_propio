"""
Real Materials Data Loader for Autoresearch (Phase 4).
Downloads formation energy data from JARVIS-DFT (NIST) or Figshare.
No API key required. Sovereign operation.

Usage:
    python load_real_data.py              # Download and prepare dataset
    python load_real_data.py --source figshare  # Use Figshare CSV instead
"""

import os
import json
import csv
import math
import random
import requests
import torch
import numpy as np

CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "autoresearch", "real_data")
MATERIALS_FILE = os.path.join(CACHE_DIR, "formation_energies.json")

# Figshare dataset: curated formation energies from SSUB/OQMD
FIGSHARE_URL = "https://figshare.com/ndownloader/files/23508293"
FIGSHARE_FILE = os.path.join(CACHE_DIR, "formation_energies_figshare.csv")

# JARVIS-DFT: Full 3D materials dataset 
JARVIS_URL = "https://figshare.com/ndownloader/files/40084921"  # jvasp 3d
JARVIS_FILE = os.path.join(CACHE_DIR, "jvasp_3d.json")


def download_file(url, dest):
    """Download a file with progress reporting."""
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest):
        print(f"  [CACHED] {dest}")
        return True
    print(f"  Downloading {url}...")
    try:
        r = requests.get(url, stream=True, timeout=120)
        r.raise_for_status()
        total = int(r.headers.get('content-length', 0))
        downloaded = 0
        with open(dest + ".tmp", "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += len(chunk)
                if total > 0:
                    pct = downloaded / total * 100
                    print(f"\r  Progress: {pct:.1f}% ({downloaded}/{total} bytes)", end="", flush=True)
        os.rename(dest + ".tmp", dest)
        print(f"\n  [OK] Saved to {dest}")
        return True
    except Exception as e:
        print(f"\n  [ERROR] Download failed: {e}")
        if os.path.exists(dest + ".tmp"):
            os.remove(dest + ".tmp")
        return False


def load_jarvis_data():
    """Load JARVIS-DFT 3D materials data. Returns list of (formula, formation_energy_per_atom)."""
    if not download_file(JARVIS_URL, JARVIS_FILE):
        return None
    
    print("  Parsing JARVIS-DFT data...")
    with open(JARVIS_FILE, "r") as f:
        data = json.load(f)
    
    entries = []
    for item in data:
        fe = item.get("formation_energy_peratom")
        formula = item.get("formula", "Unknown")
        if fe is not None and not math.isnan(fe):
            entries.append({
                "formula": formula,
                "formation_energy_peratom": float(fe),
                "jid": item.get("jid", ""),
                "spacegroup": item.get("spg_symbol", ""),
                "bandgap": item.get("optb88vdw_bandgap", None)
            })
    
    print(f"  [OK] Loaded {len(entries)} materials with formation energies")
    return entries


def load_figshare_data():
    """Load Figshare CSV formation energy dataset. Fallback if JARVIS fails."""
    if not download_file(FIGSHARE_URL, FIGSHARE_FILE):
        return None
    
    print("  Parsing Figshare CSV...")
    entries = []
    with open(FIGSHARE_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                fe = float(row.get("formation_energy", row.get("Formation Energy", 0)))
                formula = row.get("formula", row.get("Formula", "Unknown"))
                entries.append({
                    "formula": formula,
                    "formation_energy_peratom": fe,
                })
            except (ValueError, TypeError):
                continue
    
    print(f"  [OK] Loaded {len(entries)} entries from Figshare")
    return entries


def prepare_train_val_split(entries, val_ratio=0.1, seed=42):
    """Split data into train/val sets and save as tensors."""
    random.seed(seed)
    random.shuffle(entries)
    
    n_val = max(1, int(len(entries) * val_ratio))
    val_data = entries[:n_val]
    train_data = entries[n_val:]
    
    # Convert to tensors for evaluation
    val_energies = torch.tensor([e["formation_energy_peratom"] for e in val_data], dtype=torch.float32)
    train_energies = torch.tensor([e["formation_energy_peratom"] for e in train_data], dtype=torch.float32)
    
    # Save
    torch.save(val_energies, os.path.join(CACHE_DIR, "val_energies.pt"))
    torch.save(train_energies, os.path.join(CACHE_DIR, "train_energies.pt"))
    
    # Save metadata
    with open(os.path.join(CACHE_DIR, "data_summary.json"), "w") as f:
        json.dump({
            "total_entries": len(entries),
            "train_size": len(train_data),
            "val_size": len(val_data),
            "mean_energy": float(np.mean([e["formation_energy_peratom"] for e in entries])),
            "std_energy": float(np.std([e["formation_energy_peratom"] for e in entries])),
            "min_energy": float(min(e["formation_energy_peratom"] for e in entries)),
            "max_energy": float(max(e["formation_energy_peratom"] for e in entries)),
        }, f, indent=2)
    
    print(f"\n  Dataset Summary:")
    print(f"    Train: {len(train_data)} | Val: {len(val_data)}")
    print(f"    Energy range: [{min(e['formation_energy_peratom'] for e in entries):.4f}, {max(e['formation_energy_peratom'] for e in entries):.4f}] eV/atom")
    print(f"    Mean: {np.mean([e['formation_energy_peratom'] for e in entries]):.4f} eV/atom")
    
    return train_data, val_data


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", choices=["jarvis", "figshare"], default="jarvis")
    args = parser.parse_args()
    
    print("--- Autoresearch: Real Materials Data Loader (Phase 4) ---\n")
    
    if args.source == "jarvis":
        entries = load_jarvis_data()
    else:
        entries = load_figshare_data()
    
    if entries is None or len(entries) == 0:
        print("[FALLBACK] Trying Figshare...")
        entries = load_figshare_data()
    
    if entries and len(entries) > 0:
        train_data, val_data = prepare_train_val_split(entries)
        print(f"\n[OK] Real data ready at {CACHE_DIR}")
        print("     Use val_energies.pt for ground truth evaluation.")
    else:
        print("[ERROR] No data could be loaded. Check internet connection.")
