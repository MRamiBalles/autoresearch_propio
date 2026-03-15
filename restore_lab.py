import subprocess
import os
import time

def run_bg(cmd, log):
    print(f"Lanzando: {cmd}")
    # Usamos una forma más compatible de PowerShell para lanzar en segundo plano con redirección
    full_cmd = f"Start-Process powershell -ArgumentList '-NoProfile -Command \"{cmd} >> {log} 2>&1\"' -WindowStyle Hidden"
    subprocess.Popen(["powershell", "-Command", full_cmd], shell=True)

if __name__ == "__main__":
    print("--- Autoresearch Lab Restoration (Shadow Swarm) ---")
    time.sleep(2)
    
    # Definimos los comandos y sus respectivos logs
    jobs = [
        ("$env:RESEARCH_MODE='medical'; python train.py --warmup-steps 100", "research_long.log"),
        ("$env:RESEARCH_MODE='materials'; python train.py --num-iterations 500 --warmup-steps 100", "swarm_node_01-Materials.log"),
        ("$env:RESEARCH_MODE='medical'; python train.py --num-iterations 500 --warmup-steps 100", "swarm_node_02-Medical-Scout.log"),
        ("python shadow_swarm_orchestrator.py", "shadow_orchestrator.log")
    ]
    
    for cmd, log in jobs:
        run_bg(cmd, log)
        time.sleep(1) # Pausa breve entre lanzamientos
    
    print("\n[OK] Lab restaurado. El Shadow Swarm está operando en segundo plano.")
    print("Verifique el estado en 'swarm_status.md' en unos instantes.")
