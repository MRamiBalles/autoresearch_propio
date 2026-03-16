# Paper: Arquitecturas Supramoleculares y Descubrimiento Agéntico de Materiales

## Abstract
**Objetivo**: Automatización del diseño y manipulación estructural de marcos orgánicos covalentes (COFs) mediante ingeniería agéntica, centrada en la predicción de estabilidad tras la escisión de macrociclos.
**Metodología**: Implementación de un enjambre agéntico que utiliza técnicas de **"Clip-off Chemistry"** (Sánchez-Naya et al., Science 2025) para simular la eliminación selectiva de bloques orgánicos y predecir la integridad de la red isoreticular.
**Resultados**: Reducción del MAE a **1.0008 eV** en la predicción de energías de enlace de macrociclos extraídos en hardware soberano (CPU).

## Fundamentación Científica
Este trabajo se basa en los avances pioneros de **Roberto Sánchez-Naya** (ORCID: 0000-0001-7145-266X) en el ICN2, específicamente en la manipulación atómica de sólidos porosos cristalinos. La integración de estos principios químicos en el espacio latente de nuestros modelos `autoresearch` permite una exploración del espacio de materiales alineada con las leyes de la química supramolecular.

## Estructura del Proyecto
- `src/`: Lógica de predicción de energía basada en descriptores cristalográficos.
- `tests/`: Validación de estabilidad estructural (Node isolation protocol).
- `results/`: Persistencia de métricas en `results.tsv`.
- `papers/`: Borradores para sumisión a *Nature Materials*.
