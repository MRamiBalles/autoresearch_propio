# Research Improvement Program

Este archivo define las directrices para que un agente autónomo mejore la calidad de la guía de entrevista de Manuel.

## 1. El Objetivo (The Metric)
Maximizar el **Puntaje de Relevancia (PR)** del documento `guru_sup_interview_prep.md`.

### Criterios de Evaluación:
- **Novedad**: ¿Contiene información de las últimas 48 horas (X/LinkedIn de Víctor Mollá)?
- **Profundidad Técnica**: ¿Explica fallos de LLM y soluciones de arquitectura?
- **Claridad de Negocio**: ¿Conecta la técnica con los 20k de MRR y la ronda de inversión?

## 2. El Loop de Entrenamiento (5min wall-clock)
Para cada iteración, el agente debe:
1. Leer los archivos en `schemes_v1`.
2. Realizar una búsqueda web rápida sobre "GuruSup", "Víctor Mollá" o "Salespath AI" para detectar novedades.
3. Proponer una mejora específica en un bloque de texto.
4. Simular la respuesta de Bruno ante ese nuevo dato.
5. Si Bruno queda "Wowed" (impresionado), integrar el cambio.

## 3. Instrucciones de Seguridad
- No borrar la información core sobre PydanticAI.
- No inventar datos financieros que no sean públicos.
- Mantener el tono de "Ingeniería de Agentes".

---
*Fase de entrenamiento iniciada. Generación: 001.*
