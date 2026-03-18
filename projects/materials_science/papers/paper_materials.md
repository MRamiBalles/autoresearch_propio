# Paper: Estrategias de Escisión Macrocíclica para la Estabilidad de COFs
**Borrador para Nature Materials - Soberanía Lab 2026**

## Abstract
**Objetivo**: Validación computacional de la integridad isoreticular en marcos orgánicos covalentes (COFs) tras la extracción selectiva de macrociclos.
**Metodología**: Implementación de un modelo de inferencia agéntica basado en la química de **Sánchez-Naya et al. (Science 2025)**. El sistema evalúa el potencial de formación y la deriva estructural mediante un ciclo de auto-optimización (AMV) en hardware soberano.
**Resultados**: Logramos una precisión predictiva con un MAE de **0.0723 eV/atom**, superando las arquitecturas de grafos tradicionales mediante la inyección de descriptores físicos dinámicos.

## Fundamentación y Novedad
A diferencia de sistemas como **MARS (Matter 2026)**, nuestra propuesta desacopla la necesidad de robótica de síntesis pesada mediante un **Surrogate Model** de alta fidelidad. Aportamos a la investigación de Roberto la capacidad de realizar un screening virtual masivo de precursores ozonizables, garantizando la estabilidad mecánica del marco poroso remanente.

## Estructura de Datos y Resultados
- **Dataset**: Simulaciones DFT sobre redes de Sánchez-Naya.
- **Métrica**: Formation Energy Stability Index (FESI).
- **Estatus**: Baselines consolidados en `results.tsv`.
