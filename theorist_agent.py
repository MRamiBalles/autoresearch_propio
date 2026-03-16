import os
import pandas as pd
import torch
from datetime import datetime

# ---------------------------------------------------------------------------
# Agente Teórico: Razonamiento sobre Resultados Científicos
# ---------------------------------------------------------------------------

RESULTS_FILE = "results.tsv"
HYPOTHESES_FILE = os.path.join(os.path.expanduser("~"), ".cache", "autoresearch", "hypotheses.md")

def analyze_results():
    if not os.path.exists(RESULTS_FILE):
        print(f"Error: {RESULTS_FILE} not found.")
        return None

    df = pd.read_csv(RESULTS_FILE, sep='\t')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    analysis = []
    for mode in df['mode'].unique():
        mode_df = df[df['mode'] == mode].sort_values('timestamp')
        if len(mode_df) < 2:
            analysis.append(f"  - [{mode.upper()}] Insufficient data for trend analysis.")
            continue
            
        last_metric = mode_df['metric_value'].iloc[-1]
        prev_metric = mode_df['metric_value'].iloc[-2]
        improvement = prev_metric - last_metric
        
        status = "IMPROVING" if improvement > 0 else "PLATEAU/REGRESSING"
        analysis.append(f"  - [{mode.upper()}] Current: {last_metric:.6f} | Trend: {status} ({improvement:+.6f})")
        
    return "\n".join(analysis)

def generate_hypotheses(analysis_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    hypothesis_content = f"""# Reporte de Hipótesis del Agente Teórico
Generado: {timestamp}

## Análisis de Convergencia
{analysis_text}

## Hipótesis Sugeridas (Fase 7)

### 1. Dominio de Materiales (JARVIS-DFT)
- **Hipótesis**: La inyección de descriptores de Spacegroup ha reducido el MAE residual al proporcionar una base de simetría que el modelo antes debía inferir de los tokens.
- **Predicción**: Un aumento en la profundidad de la proyección (`physics_proj`) podría capturar interacciones no lineales entre densidad y energía de formación.

### 2. Dominio Médico (Nganga Line)
- **Hipótesis**: La penalización de Hot Spots (DVH) está forzando al modelo a aprender distribuciones de dosis más suaves, lo que estabiliza el MAE pero puede enlentecer la convergencia inicial.
- **Predicción**: Un scheduler de LR más agresivo en la fase de 'warmdown' podría ayudar a escapar de mínimos locales creados por las restricciones de seguridad.

## Plan de Acción Recomendado
1. Ejecutar ciclo de 24h con `MATRIX_LR=0.05` para probar la elasticidad del modelo en Materiales.
2. Monitorizar el `peer_review_agent` para asegurar que las hipótesis no violan la termodinámica básica.

---
**Soberanía Científica Autoresearch 2026**
"""
    
    os.makedirs(os.path.dirname(HYPOTHESES_FILE), exist_ok=True)
    with open(HYPOTHESES_FILE, "w", encoding="utf-8") as f:
        f.write(hypothesis_content)
    
    print(f"Hypotheses generated at {HYPOTHESES_FILE}")
    return hypothesis_content

if __name__ == "__main__":
    print("--- Theorist Agent Online ---")
    analysis = analyze_results()
    if analysis:
        print("Analysis complete:")
        print(analysis)
        generate_hypotheses(analysis)
    else:
        print("Waiting for more data to theorize...")
