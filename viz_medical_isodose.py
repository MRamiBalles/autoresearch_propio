"""
Sovereignty Dashboard 2.0: Real-time Isodose Visualization (Nganga Line).
Visualizes the TG-43 radiation field around a brachytherapy seed.
Allows the user to see the "Physics" behind the model predictions.
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import json

CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "autoresearch", "real_data", "medical")
OUTPUT_PATH = "d:/autoresearch/isodose_map.png"

def generate_isodose_map(seed_x=0, seed_y=0, Sk=1.0, precision=100):
    """
    Generate a 2D isodose map using the validated TG-43 engine.
    """
    # Grid: -5cm to 5cm
    x = np.linspace(-5, 5, precision)
    y = np.linspace(-5, 5, precision)
    X, Y = np.meshgrid(x, y)
    
    # Distance R from seed
    R = np.sqrt((X - seed_x)**2 + (Y - seed_y)**2)
    
    # TG-43 1D approximation (Parameters from generate_medical_data.py)
    Lambda = 0.925
    G_POLY = [0.9922, 0.05739, -0.05353, 0.009315, -0.0006734]
    
    # Calculate G (Geometry factor 1/r^2)
    # Avoid singularity at r=0
    R_safe = np.where(R < 0.1, 0.1, R)
    G = 1.0 / (R_safe**2)
    
    # Radial dose function g(r)
    g_r = (G_POLY[0] + G_POLY[1]*R_safe + G_POLY[2]*(R_safe**2) + 
           G_POLY[3]*(R_safe**3) + G_POLY[4]*(R_safe**4))
    
    # Dose Rate
    Dose = Sk * Lambda * G * g_r
    
    # Mask very high values near seed for visualization
    Dose = np.where(R < 0.2, Dose.max() * 1.5, Dose)
    
    plt.figure(figsize=(10, 8), facecolor='#111111')
    ax = plt.gca()
    ax.set_facecolor('#111111')
    
    # Plot heatmap
    levels = [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
    cp = plt.contourf(X, Y, Dose, levels=levels, cmap='magma', alpha=0.8)
    plt.colorbar(cp, label='Dose Rate (Gy/h)')
    
    # Plot specific isodose lines
    contours = plt.contour(X, Y, Dose, levels=[0.1, 0.5, 1.0], colors='cyan', linestyles='dashed', linewidths=1)
    plt.clabel(contours, inline=True, fontsize=10, fmt='%.1f Gy/h')
    
    # Mark seed
    plt.scatter([seed_x], [seed_y], color='white', marker='*', s=200, label='125I Seed (Oncura 6711)')
    
    plt.title("Nganga Line: Physical Isodose Map (TG-43 Validated)", color='white', pad=20)
    plt.xlabel("Distance X (cm)", color='white')
    plt.ylabel("Distance Y (cm)", color='white')
    plt.grid(color='#333333', linestyle='--', alpha=0.5)
    plt.legend()
    
    # Style tweaks
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('#444444')
        
    plt.tight_layout()
    plt.savefig(OUTPUT_PATH, dpi=150)
    print(f"  [OK] Isodose map saved to: {OUTPUT_PATH}")
    return OUTPUT_PATH

if __name__ == "__main__":
    generate_isodose_map()
