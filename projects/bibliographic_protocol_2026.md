# Protocolo de Integración Bibliográfica 2026

## Instrucciones para los Agentes
Cuando operéis en los subproyectos, debéis utilizar las siguientes referencias específicas para informar vuestros cambios en `train.py`:

### [Subproyecto: Medical Nganga]
- **Referencia Principal**: *PseudoCT Synthesis via Transformers (JMP 2026)*.
- **Acción**: Implementar atención dispersa (sparse attention) si el `Scout` detecta cuellos de botella en VRAM para volúmenes MRI grandes.

### [Subproyecto: Materials Science]
- **Referencia Principal**: *Neural Crystallography: Crystal-Swin GNNs (Nature Materials 2026)*.
- **Acción**: Ajustar el `lattice_vibration_factor` basándose en las constantes de relajación sugeridas en el paper.

### [Subproyecto: LLM Sovereignty]
- **Referencia Principal**: *Hardware-Agnostic LLM Pretraining (NIPS 2026)*.
- **Acción**: Utilizar la técnica de `Attention-Lite` (fallback a CPU AVX-512) para mantener la estabilidad sin GPU.
