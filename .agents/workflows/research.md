---
description: Flujo de investigación técnica y automatización de revisión de literatura IA
---

# Flujo de Investigación Autovisionado (AI Research Workflow)

Este workflow automatiza la fase de investigación para nuevos agentes en GuruSup utilizando la filosofía de Medina Sandín.

## Fase 1: Recolección y Triage
1. **Búsqueda**: Usa Elicit/Consensus para papers o GitHub Search para repos.
2. **Criba Rápida (Prompt 6)**:
   > "Actúa como un CTO evaluando tecnología. Analiza este [Abstract/README] y dime las 3 innovaciones técnicas reales que aporta. Si no mejora la latencia o la confiabilidad, descártalo."

## Fase 2: Extracción y Gap Analysis (El "Cerebro")
3. **Extracción (Prompt 7)**:
   > "Extrae la arquitectura lógica de este sistema y represéntala en una matriz de componentes. ¿Cómo manejan el estado del agente y la recuperación de errores?"
4. **Búsqueda de Brechas (Prompt 2 - Adaptado)**:
   > "Basado en estos 5 repos de State-of-the-art, identifica qué brecha técnica hay en la orquestación actual de Salespath. Crea un 'Elevator Pitch' técnico para proponer una mejora."

## Fase 3: Arquitectura y Validación
5. **Architect Review (Prompt 4)**:
   > "Actúa como un arquitecto senior de IA. Critica mi diseño de [Nueva Funcionalidad]. Sé implacable con la escalabilidad y el coste de tokens (Token Burn)."
6. **Executive Briefing (Prompt 8)**:
   > "Escribe un resumen técnico para Víctor Mollá explicando la ganancia de val_bpb que esperamos tras este experimento."

// turbo
7. **Plan de Sprint (Prompt 9)**:
   > "Crea un cronograma de 48h de experimentos autónomos de 'autoresearch' para validar esta idea mientras el equipo descansa."
