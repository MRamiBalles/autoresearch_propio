"""
Material Discovery Scout (Fase 5).
Searches the validated JARVIS-DFT dataset for the most stable materials.
Goal: Identify top 10 candidates with minimum formation energy (maximum stability).
Reference: NIST JARVIS-DFT Database (75,993 materials).
"""

import os
import json
import torch
import pandas as pd

CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "autoresearch", "real_data")
SUMMARY_FILE = os.path.join(CACHE_DIR, "data_summary.json")
SAMPLE_FILE = os.path.join(CACHE_DIR, "sample_entries.json")

def discover_stable_materials(n_candidates=10):
    print("--- Autoresearch Material Discovery: Scanning NIST JARVIS-DFT ---")
    
    # In a real scenario, we would load the full 75k entries.
    # For the POC, we use the jarvis-tools to fetch the best candidates efficiently.
    try:
        from jarvis.db.figshare import data as jdata
        print("Fetching real DFT data from JARVIS...")
        data = jdata('dft_3d')
    except Exception as e:
        print(f"Error fetching data: {e}. Falling back to pre-processed samples.")
        if os.path.exists(SAMPLE_FILE):
            with open(SAMPLE_FILE, "r") as f:
                data = json.load(f)
        else:
            return None

    print(f"Scanning {len(data):,}, materials...")

    # Filter for valid formation energy and sort by it (lower is more stable)
    candidates = []
    for d in data:
        fe = d.get("formation_energy_peratom")
        if fe is not None:
            candidates.append({
                "jid": d.get("jid"),
                "formula": d.get("formula"),
                "formation_energy": float(fe),
                "spacegroup": d.get("spg_symbol"),
                "bandgap": d.get("optb88vdw_bandgap"),
                "ehull": d.get("ehull")
            })
    
    # Sort by stability (formation energy)
    candidates.sort(key=lambda x: x["formation_energy"])
    
    top_10 = candidates[:n_candidates]
    
    print(f"\nTop {n_candidates} Most Stable Materials Discovered:")
    print(f"{'JID':<15} | {'Formula':<15} | {'E_form (eV/atom)':<20} | {'Spacegroup':<12}")
    print("-" * 70)
    for c in top_10:
        print(f"{c['jid']:<15} | {c['formula']:<15} | {c['formation_energy']:<20.6f} | {c['spacegroup']:<12}")
    
    # Save discovery report
    report = {
        "discovery_date": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": "JARVIS-DFT 3D",
        "total_scanned": len(data),
        "top_candidates": top_10
    }
    
    output_path = "d:/autoresearch/discovered_materials.json"
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"\n[OK] Discovery report saved to: {output_path}")
    return top_10

if __name__ == "__main__":
    discover_stable_materials()
