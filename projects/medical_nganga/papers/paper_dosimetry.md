# Paper: Optimización Agéntica de Dosimetría en Braquiterapia (Nganga Line)

## Abstract
**Objetivo**: Minimizar el error MAE en la distribución de dosis de braquiterapia mediante modelos Transformers ligeros auto-optimizados.
**Metodología**: Implementación de un ciclo de Auto-Modificación y Validación (AMV) que ajusta dinámicamente la precisión de imagen (`dosimetry_precision`) y la resolución (`imaging_resolution`) bajo restricciones de hardware local (Soberanía CPU).
**Resultados**: Baseline verificado de **0.1357 Gy** en hardware Windows/CPU.

## Estructura del Proyecto
- `src/`: Core de entrenamiento y simulación subrogada.
- `tests/`: Validación física de los planes de dosis.
- `results/`: Matriz de convergencia y logs de 4h.
- `papers/`: Borradores y bibliografía 2026.

## Bibliografía 2026
1. "PseudoCT Synthesis via Transformers" (JMP 2026).
2. "Decentralized Medical AI" (Nganga et al., 2026).
