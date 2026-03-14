# Sistema de Optimización de Investigación (vía Autoresearch)

Para mejorar el "proyecto base" (toda la investigación de GuruSup) usando la filosofía de Karpathy, trataremos la **Guía de Preparación** como si fuera el `train.py` y los **Criterios de Excelencia** como el `val_bpb`.

## 1. El Concepto Meta-Investigativo
En lugar de optimizar pesos de una red neuronal, optimizamos la **densidad de valor** de tu investigación.

- **Fichero a optimizar (`research.md`)**: El documento que contiene tu estrategia para la entrevista.
- **Fichero de control (`program.md`)**: Las instrucciones para un agente (yo o un sub-agente) para que busque fallos o vacíos.
- **Métrica (`research_score`)**: Una puntuación del 0 al 10 basada en:
    - Precisión técnica (¿usa términos como PydanticAI/Go correctly?).
    - Alineación con el negocio (¿menciona el ROI/Product-Market fit?).
    - Rareza (¿aporta datos que no están en la primera página de Google?).

## 2. El Bucle de Mejora Autónoma
Puedes ejecutar este "bucle" conmigo:

1. **PROPOSICIÓN**: El sistema analiza el estado actual y propone añadir un detalle (ej: "Añadir gestión de 'Sliding Windows' para el contexto de los agentes").
2. **SIMULACIÓN**: Se integra el cambio en una copia temporal de la guía.
3. **EVALUACIÓN**: Un agente "Crítico de GuruSup" evalúa el nuevo documento.
4. **KEEP/DISCARD**: Si el `research_score` sube, se actualiza la guía principal.

## 3. Implementación Práctica en tu Folder
He preparado el archivo `research_program.md` en tu carpeta `schemes_v1`. Este archivo contiene las instrucciones para "entrenar" tu investigación:

### Qué investigar para mejorar el "Score":
- **Nuevos Tweets de Víctor Mollá**: Sus opiniones cambian rápido; el agente debe monitorizar su X/Twitter.
- **Updates de PydanticAI**: Si sale una versión nueva, la guía debe actualizarse.
- **Casos de éxito de Salespath**: Buscar testimonios reales de clientes actuales para usarlos como ejemplos en la entrevista.

---

> [!TIP]
> Al decirle a Bruno que has usado un **bucle de optimización autónoma para mejorar tu propia preparación de la entrevista**, estarás demostrando en tiempo real que eres el "Software Engineer - LLMs & GenAI" que necesitan.
