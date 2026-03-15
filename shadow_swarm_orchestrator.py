import os
import time
import glob
from datetime import datetime

# Configuración del Orquestador
RESULTS_LOG = "results.tsv"
REPORT_FILE = "swarm_status.md"

def get_last_metrics(log_path):
    try:
        if not os.path.exists(log_path):
            return "N/A", "N/A"
        with open(log_path, "r") as f:
            lines = f.readlines()
            if not lines:
                return "N/A", "N/A"
            # Buscamos de abajo hacia arriba la última línea con 'step'
            for line in reversed(lines):
                if "step" in line and "|" in line:
                    parts = line.split("|")
                    step_val = parts[0].strip()
                    loss_val = "N/A"
                    for p in parts:
                        if "loss:" in p:
                            loss_val = p.split(":")[1].strip()
                    return step_val, loss_val
    except Exception:
        pass
    return "N/A", "N/A"

def sync_findings():
    print(f"[{datetime.now()}] Shadow Swarm: Sincronizando hachazgos...")
    
    status_report = "# Estado de Shadow Swarm (Enjambre de Laboratorios)\n\n"
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status_report += f"Última sincronización: {now_str}\n\n"
    status_report += "| Nodo | Modo | Último Paso | Loss | Estado |\n"
    status_report += "| :--- | :--- | :--- | :--- | :--- |\n"
    
    log_files = glob.glob("swarm_node_*.log")
    # Agregamos también el log principal si existe
    if os.path.exists("research_long.log"):
        log_files.append("research_long.log")
    
    for log in log_files:
        node_name = log.replace("swarm_node_", "").replace(".log", "")
        if "research_long" in node_name:
            node_name = "Master-Long-Term"
            mode = "medical"
        else:
            mode = "materials" if "Materials" in node_name else "medical"
            
        step, loss = get_last_metrics(log)
        status = "Activo" if step != "N/A" else "Iniciando"
        status_report += f"| {node_name} | {mode} | {step} | {loss} | {status} |\n"

    with open(REPORT_FILE, "w") as f:
        f.write(status_report)
    print(f"  > Reporte '{REPORT_FILE}' actualizado.")

def orchestrate_cycle():
    while True:
        sync_findings()
        time.sleep(60) 

if __name__ == "__main__":
    print("--- Autoresearch Shadow Swarm Orchestrator (Phase 3) ---")
    orchestrate_cycle()
