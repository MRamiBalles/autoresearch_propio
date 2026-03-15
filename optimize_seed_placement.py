"""
SPO: Stereotactic Plan Optimizer (Nganga Line).
Uses the TG-43 physics engine to find optimal seed placement (Inverse Planning).
Goal: Maximize dose at Target Center while keeping OAR Dose < Limit.
"""

import numpy as np
from scipy.optimize import minimize
import os
import json

# TG-43 Physics Parameters (NIST/Carleton Validated)
LAMBDA = 0.925
G_POLY = [0.9922, 0.05739, -0.05353, 0.009315, -0.0006734]

def get_dose_at_point(point, seed_pos, Sk=1.0):
    """Calculate dose at a specific point [x, y] from a seed at [sx, sy]."""
    r = np.sqrt(np.sum((point - seed_pos)**2))
    if r < 0.1: r = 0.1 # Physical catheter limit
    
    # Geometry factor
    G = 1.0 / (r**2)
    # Radial dose function
    g_r = G_POLY[0] + G_POLY[1]*r + G_POLY[2]*(r**2) + G_POLY[3]*(r**3) + G_POLY[4]*(r**4)
    return Sk * LAMBDA * G * g_r

def objective_function(seed_coords, target_points, oar_points, dose_threshold=1.0):
    """
    Cost function to minimize.
    - Negative of Target Dose (we want to maximize it)
    - Penalty for OAR Dose (if > threshold)
    """
    sx, sy = seed_coords
    seed_pos = np.array([sx, sy])
    
    # 1. Target Dose (Mean dose to target points)
    target_doses = [get_dose_at_point(p, seed_pos) for p in target_points]
    mean_target_dose = np.mean(target_doses)
    
    # 2. OAR Dose Penalty
    oar_doses = [get_dose_at_point(p, seed_pos) for p in oar_points]
    max_oar_dose = np.max(oar_doses)
    
    # Penalty: Square of dose above threshold
    penalty = 0
    if max_oar_dose > dose_threshold:
        penalty = 100 * (max_oar_dose - dose_threshold)**2
        
    # 3. Hot Spot Penalty (Dose too high in any point)
    hot_spot_limit = 60.0 # Gy/h - Threshold for potential necrosis
    all_doses = target_doses + oar_doses
    max_dose = np.max(all_doses)
    
    hot_spot_penalty = 0
    if max_dose > hot_spot_limit:
        hot_spot_penalty = 50 * (max_dose - hot_spot_limit)**2
        
    # Total cost (Maximize Target, Minimize OAR Penalty, Minimize Hot Spot Penalty)
    return -mean_target_dose + penalty + hot_spot_penalty

def run_optimization():
    print("--- Autoresearch SPO: Starting Inverse Planning (Nganga Line) ---")
    
    # Define Clinical Scenario:
    # Tumor (Target) at [2.0, 2.0]
    target_center = np.array([2.0, 2.0])
    target_points = [target_center + np.random.normal(0, 0.2, 2) for _ in range(10)]
    
    # Organ at Risk (OAR) at [0.0, 0.0] (e.g., Urethra or Rectum)
    oar_center = np.array([0.0, 0.0])
    oar_points = [oar_center + np.random.normal(0, 0.1, 2) for _ in range(5)]
    
    # Starting guess: seed at origin
    initial_guess = [0.0, 0.0]
    
    # Optimization (minimize cost)
    res = minimize(objective_function, initial_guess, 
                  args=(target_points, oar_points, 0.5), # Limit OAR to 0.5 Gy/h
                  method='Nelder-Mead')
    
    opt_x, opt_y = res.x
    print(f"\nOptimization Result:")
    print(f"  Optimal Seed Coords: [{opt_x:.4f}, {opt_y:.4f}]")
    print(f"  Predicted Target Dose: {abs(res.fun):.4f} Gy/h")
    
    # Final check of OAR dose
    oar_dose = np.max([get_dose_at_point(p, np.array([opt_x, opt_y])) for p in oar_points])
    print(f"  Max OAR Dose: {oar_dose:.4f} Gy/h (Limit: 0.5)")
    
    # Save clinical plan
    plan = {
        "case_id": "ST-NGANGA-001",
        "optimization_status": "Converged" if res.success else "Failed",
        "optimal_coords": [opt_x, opt_y],
        "target_dose_gyh": abs(res.fun),
        "oar_dose_gyh": oar_dose,
        "parameters": "TG-43_125I_Oncura_6711",
    }
    
    with open("d:/autoresearch/optimal_clinical_plan.json", "w") as f:
        json.dump(plan, f, indent=2)
    
    print("\n[OK] Optimal clinical plan saved to: d:/autoresearch/optimal_clinical_plan.json")
    return plan

if __name__ == "__main__":
    run_optimization()
