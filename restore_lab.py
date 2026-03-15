import subprocess
import os
import time

def run_bg(cmd, log):
    print(f"Lanzando: {cmd}")
    # Redirección nativa de PowerShell para evitar bloqueos
    p_cmd = f"Start-Process powershell -ArgumentList '-Command \"{cmd} >> {log} 2>&1\"' -WindowStyle Hidden"
    subprocess.Popen(["powershell", "-Command", p_cmd], shell=True)

if __name__ == "__main__":
    print("--- Autoresearch Lab Restoration (Shadow Swarm) ---")
    time.sleep(5) # Espera prolongada para liberar archivos
    
    # 1. Master Long-Term (Medical)
    run_bg("$env:RESEARCH_MODE='medical'; python train.py --warmup-steps 100", "research_long.log")
    
    # 2. Swarm Nodes (Materials & Medical Scout)
    run_bg("$env:RESEARCH_MODE='materials'; python train.py --num-iterations 100 --warmup-steps 10", "swarm_node_01-Materials.log")
    run_bg("$env:RESEARCH_MODE='medical'; python train.py --num-iterations 100 --warmup-steps 10", "swarm_node_02-Medical-Scout.log")
    
    # 3. Orchestrator
    run_bg("python shadow_swarm_orchestrator.py", "shadow_orchestrator.log")
    
    print("\n[OK] Lab restaurado. Verifique swarm_status.md en 60s.")
