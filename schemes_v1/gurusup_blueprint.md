# Blueprint: Cómo se construye una empresa como GuruSup

Si tuvieras que fundar GuruSup mañana, o si Bruno te pregunta cómo escalarías la visión actual, estos son los pilares fundamentales y los detalles que deberías investigar.

## 1. Los 3 Pilares de Construcción

### A. La Capa de Integración (The "Hands")
Una empresa de agentes no vale nada si solo habla. Su valor está en la **acción**.
- **Building Strategy**: En lugar de programar cada API a mano (Salesforce, HubSpot, etc.), se construye una **capa de abstracción de herramientas**. El agente pide `search_customer(email)` y el sistema sabe qué API llamar según el cliente.
- **Detalle interesante**: Investiga sobre herramientas como **Unified APIs** (ej: Merge.dev o Rutter) que GuruSup podría estar usando para no morir manteniendo integraciones.

### B. El Cerebro Multi-Inquilino (The "Multi-tenant Brain")
Cómo gestionar miles de agentes para cientos de empresas distintas sin que se mezclen los datos.
- **Building Strategy**: Arquitectura orientada a eventos. Cada "ticket" o "lead" dispara un workflow agéntico aislado.
- **Optimización de Costes**: Usar modelos pequeños (Haiku, Flash) para tareas de clasificación y modelos grandes (Pro, Opus) solo para decisiones críticas o redacción final.

### C. El Foso de Datos (The "Moat")
El código de un agente es fácil de copiar; los **datos de resolución** no.
- **Building Strategy**: Implementar un bucle donde cada vez que un humano corrige al agente (Human-in-the-loop), esa corrección se convierte en un nuevo "Few-shot example" para el RAG.
- **La ventaja competitiva**: GuruSup sabe "cómo respondería un experto" porque han procesado millones de tickets históricos de GuruWalk y otros clientes.

## 2. "Hotspots" de Investigación (Preguntas para Bruno/Víctor)

Para demostrar que piensas como un socio y no solo como un empleado, investiga/pregunta estos puntos "calientes":

1.  **Unit Economics & Token Burn**: *"¿Cómo gestionáis el balance entre el coste de tokens de modelos como Gemini 1.5 Pro y el valor que percibe el cliente por cada ticket resuelto?"* (Esto demuestra que te importa la rentabilidad).
2.  **Agent Drift & Hallucinations**: *"¿Cómo monitorizáis la 'deriva' de los agentes? ¿Usáis alguna herramienta tipo LangSmith para ver si un cambio en el prompt de Salespath está afectando negativamente a otros flujos?"*
3.  **Privacy & Compliance**: *"Dado que Salespath escrapea internet y GuruSup lee tickets con datos sensibles, ¿cómo manejáis la anonimización de datos (PII) antes de enviarlos a los modelos de OpenAI o Google?"*
4.  **Realtime Multi-modal**: *"Con el proyecto del avatar 'Ana', ¿qué retos habéis encontrado al sincronizar el estado del agente (sus pensamientos) con la generación de voz en tiempo real para que no haya 'silencios incómodos'?"*

## 3. Lo que TÚ aportas en esta construcción

En la entrevista, posiciónate en el centro de estos tres retos:
- **Escalabilidad**: Tú vas a construir el sistema que soporte pasar de 100 a 10.000 agentes.
- **Robustez**: Tú vas a implementar los tests de PydanticAI para que el sistema sea a prueba de balas.
- **Visión Karpathy**: Tú vas a traer la cultura de la **experimentación autónoma** para que el producto mejore solo.

> [!IMPORTANT]
> GuruSup se está construyendo en la intersección de **Ingeniería de Software Tradicional** (Backends sólidos en Go/Typescript) e **Ingeniería de Agentes** (Orquestación, RAG y Prompts). Si demuestras que dominas ambos mundos, el puesto es tuyo.
