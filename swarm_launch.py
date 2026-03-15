import subprocess
import os
import time

def launch_node(node_id, mode):
    print(f"Shadow Swarm: Lanzando Nodo-{node_id} en modo {mode}...")
    log_file = f"swarm_node_{node_id}.log"
    # El comando usa el train.py del subproyecto correspondiente o el raíz
    cmd = f"$env:RESEARCH_MODE='{mode}'; python train.py --num-iterations 100 --warmup-steps 10 > {log_file} 2>&1"
    
    # Lanzamos el proceso en segundo plano (PowerShell)
    subprocess.Popen(["powershell", "-Command", cmd], shell=True)
    print(f"  > Nodo-{node_id} ejecutándose. Log: {log_file}")

if __name__ == "__main__":
    print("--- Shadow Swarm Launcher (Simulación Local) ---")
    
    # Lanzamos 2 nodos paralelos para maximizar scouting de CPU
    launch_node("01-Materials", "materials")
    launch_node("02-Medical-Scout", "medical")
    
    print("\n[INFO] Nodos lanzados. Use 'Get-Process python' para monitorizar.")
