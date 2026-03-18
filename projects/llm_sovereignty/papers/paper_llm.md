# Paper: Arquitecturas Agénticas Soberanas para la Ciencia de Materiales
**Borrador para ICLR 2026 - Hardware Sovereignty Track**

## Abstract
**Objetivo**: Desarrollo de un framework de **Agentic Engineering** capaz de orquestar el descubrimiento autónomo de materiales en hardware restringido.
**Metodología**: Implementación del patrón **AMV (Auto-Modification & Validation)** para la síntesis de código dinámico. El sistema optimiza kernels de atención para simular interacciones atómicas en COFs sin dependencia de infraestructuras GPU externas.
**Resultados**: Estabilidad de convergencia demostrada en CPUs convencionales con una latencia de ~8.7s/step, facilitando la investigación soberana en el Soberanía AI Lab.

## Contribución Técnica
Introducimos el concepto de **"Physical-In-Context Learning"**, donde el enjambre agéntico inyecta leyes de la física del estado sólido (basadas en la obra de Sánchez-Naya) directamente en los pesos del modelo. Esto permite que la IA razone sobre la integridad estructural antes de proponer cambios en el espacio de parámetros.

## Trazabilidad
- **Métricas**: `val_bpb` y `dosimetry_precision`.
- **Persistencia**: Registro inmutable de experimentos en `results.tsv` y Git.
