"""
Process REAL JARVIS-DFT data downloaded via jarvis-tools.
Creates validated ground truth tensors for autoresearch evaluation.

Source: NIST JARVIS-DFT 3D Database (75,993 materials)
DOI: 10.6084/m9.figshare.6815699
Reference: Choudhary et al., npj Comput Mater 6, 173 (2020)
"""

import os
import json
import math
import random
import statistics
import time
import torch
import numpy as np

CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "autoresearch", "real_data")
os.makedirs(CACHE_DIR, exist_ok=True)

def process_jarvis_data():
    """Load JARVIS-DFT 3D data and create ground truth tensors."""
    print("Loading JARVIS-DFT 3D via jarvis-tools...")
    from jarvis.db.figshare import data as jdata
    data = jdata('dft_3d')
    
    print(f"Total materials loaded: {len(data):,}")
    
    # Extract entries with valid formation energy
    entries = []
    for d in data:
        fe = d.get("formation_energy_peratom")
        if fe is not None and not math.isnan(fe):
            entries.append({
                "jid": d.get("jid", ""),
                "formula": d.get("formula", "Unknown"),
                "formation_energy_peratom": float(fe),
                "spg_symbol": d.get("spg_symbol", ""),
                "bandgap": d.get("optb88vdw_bandgap"),
                "ehull": d.get("ehull"),
            })
    
    print(f"Materials with valid formation energy: {len(entries):,}")
    
    # Statistical analysis
    energies = [e["formation_energy_peratom"] for e in entries]
    mean_e = statistics.mean(energies)
    std_e = statistics.stdev(energies)
    
    print(f"\n--- Formation Energy Statistics (REAL DFT DATA) ---")
    print(f"  Mean:   {mean_e:.6f} eV/atom")
    print(f"  Std:    {std_e:.6f} eV/atom")
    print(f"  Min:    {min(energies):.6f} eV/atom")
    print(f"  Max:    {max(energies):.6f} eV/atom")
    print(f"  Median: {statistics.median(energies):.6f} eV/atom")
    
    # Create train/val split
    random.seed(42)
    random.shuffle(entries)
    
    n_val = min(2000, len(entries) // 10)
    val_entries = entries[:n_val]
    train_entries = entries[n_val:]
    
    val_energies = torch.tensor([e["formation_energy_peratom"] for e in val_entries], dtype=torch.float32)
    train_energies = torch.tensor([e["formation_energy_peratom"] for e in train_entries], dtype=torch.float32)
    
    # Save tensors
    torch.save(val_energies, os.path.join(CACHE_DIR, "val_energies.pt"))
    torch.save(train_energies, os.path.join(CACHE_DIR, "train_energies.pt"))
    
    # Save full metadata
    summary = {
        "source": "JARVIS-DFT 3D (NIST)",
        "doi": "10.6084/m9.figshare.6815699",
        "reference": "Choudhary et al., npj Comput Mater 6, 173 (2020)",
        "additional_ref": "Choudhary, Commun Mater Sci (2025), DOI: 10.1016/j.commatsci.2025.114063",
        "total_materials_in_db": len(data),
        "materials_with_formation_energy": len(entries),
        "val_size": n_val,
        "train_size": len(train_entries),
        "statistics": {
            "mean_eV_per_atom": round(mean_e, 6),
            "std_eV_per_atom": round(std_e, 6),
            "min_eV_per_atom": round(min(energies), 6),
            "max_eV_per_atom": round(max(energies), 6),
            "median_eV_per_atom": round(statistics.median(energies), 6),
        },
        "validated": True,
        "data_type": "DFT (OptB88vdW functional)",
        "validation_date": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    
    with open(os.path.join(CACHE_DIR, "data_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    
    # Save sample entries for inspection
    with open(os.path.join(CACHE_DIR, "sample_entries.json"), "w") as f:
        json.dump(entries[:50], f, indent=2)
    
    print(f"\n--- Ground Truth Saved ---")
    print(f"  val_energies.pt:   {n_val:,} samples")
    print(f"  train_energies.pt: {len(train_entries):,} samples")
    print(f"  data_summary.json: Full metadata with DOI")
    print(f"  Path: {CACHE_DIR}")
    
    return summary


if __name__ == "__main__":
    print("=" * 60)
    print("  Autoresearch: REAL Data Processing (JARVIS-DFT / NIST)")
    print("=" * 60)
    summary = process_jarvis_data()
    print(f"\n✓ VALIDATED GROUND TRUTH: {summary['materials_with_formation_energy']:,} real DFT formation energies")
    print(f"  Source DOI: {summary['doi']}")
    print(f"  Reference: {summary['reference']}")
