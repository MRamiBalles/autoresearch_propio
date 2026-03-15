import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def generate_report():
    print("--- Autoresearch Sovereignty Dashboard 2026 ---")
    
    # Paths to project results
    projects = {
        "Medical (Nganga)": "results.tsv", # Using root as main source for now
        "Materials Science": "projects/materials_science/results/results.tsv",
        "LLM Sovereignty": "projects/llm_sovereignty/results/results.tsv"
    }
    
    summary_data = []
    
    for name, path in projects.items():
        if os.path.exists(path):
            try:
                df = pd.read_csv(path, sep='\t')
                last_val = df.tail(1)['metric_value'].values[0]
                status = "Active"
                summary_data.append({"Project": name, "Metric": last_val, "Status": status})
            except:
                summary_data.append({"Project": name, "Metric": "N/A", "Status": "Empty"})
        else:
            summary_data.append({"Project": name, "Metric": "N/A", "Status": "Pending"})

    summary_df = pd.DataFrame(summary_data)
    print("\n[Project Status Summary]")
    print(summary_df.to_string(index=False))
    
    # Simple Plot simulation
    if os.path.exists("results.tsv"):
        df = pd.read_csv("results.tsv", sep='\t')
        plt.figure(figsize=(10, 5))
        plt.plot(df.index, df['metric_value'], marker='o', linestyle='-', color='teal')
        plt.title('Convergence Audit: Medical/Materials Baselines')
        plt.xlabel('Experiment Index')
        plt.ylabel('Metric (MAE/BPB)')
        plt.grid(True, alpha=0.3)
        plt.savefig('sovereignty_convergence.png')
        print("\n[Plot Generated]: sovereignty_convergence.png")

    print("\n--- End of Report ---")

if __name__ == "__main__":
    generate_report()
