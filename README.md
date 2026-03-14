# autoresearch_propio (Sovereignty AI Lab)

Adaptación soberana del sistema `autoresearch` de Andrej Karpathy para la investigación en ciencia de frontera.

## Líneas de Investigación Activas

### 1. Brachytherapy Dosimetry Optimization (Edward Nganga Line)
- **Modo**: `medical`
- **Métrica**: `dose_error_mae`
- **Objetivo**: Minimizar el error de inferencia en la distribución de dosis de braquiterapia utilizando modelos subrogados basados en transformadores lite.
- **Soberanía**: Optimizado para ejecución en CPU local (Windows) sin dependencia de infraestructura Cloud propietaria.

### 2. Materials Science Accelerated Research (Próximamente)
- **Modo**: `materials`
- **Foco**: Descubrimiento de estructuras cristalinas y optimización de propiedades térmicas.

## Arquitecturas y Patrones

Este proyecto se aleja de los asistentes ReAct convencionales para implementar un flujo de **Auto-Modificación y Validación (AMV)**:
1. **Scout**: Scouting de hiperparámetros y búsquedas en la arquitectura.
2. **Analyst**: Análisis de convergencia y trade-offs entre memoria y precisión.
3. **Architect**: Re-escritura autónoma de `GPTConfig` y lógica de entrenamiento.

## 10 Palabras Clave de Innovación

1. **Agentic Code-Synthesis**
2. **Fixed-Time wall-clock Budgeting**
3. **Memory persistence via Git-Commit-History**
4. **Dosimetry surrogate MAE metric**
5. **Role-Based Swarm Delegation**
6. **Branch-Advance Logic**
7. **Hard-Constraint VRAM Management**
8. **Simplicity Criterion Optimization**
9. **Domain-Agnostic Evaluation Dispatcher**
10. **In-Context Research Literature Integration**

## Instalación

```bash
uv run prepare.py
$env:RESEARCH_MODE='medical'; uv run train.py
```

---
*Este laboratorio es una iniciativa para recuperar la soberanía científica mediante ingeniería agéntica de precisión.*
