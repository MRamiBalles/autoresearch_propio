# Deep Dive Técnico: Arquitectura, Contribución y Formación

Este documento profundiza en la ingeniería de GuruSup para que Manuel pueda hablar "de tú a tú" con el equipo técnico sobre retos reales de producción.

## 1. Arquitectura Técnica de GuruSup & Salespath

### El Sistema Multi-Agente (Orquestación)
GuruSup no usa un solo agente para todo. Su arquitectura se basa en la **especialización**:
- **Orquestador Central**: Analiza el "intent" y delega a agentes especializados (Ventas, Soporte, CRM).
- **RAG Avanzado**: No es solo una búsqueda vectorial. Implementan **Sincronización en Tiempo Real** (si el cliente cambia un dato en su web, el agente lo sabe al instante) y **Estructuración vía PydanticAI**.
- **Tool Use (Herramientas)**: Los agentes tienen "manos". Se conectan a Salesforce, HubSpot o WhatsApp para *ejecutar* acciones, no solo para hablar.

### Browser Automation (AI Lab Night & Agentic Browsing)
Uno de sus mayores retos actuales es el uso de **Playwright** con agentes:
- **Agentes Navegadores Adaptativos**: No solo scripts de Playwright, sino agentes que navegan de forma autónoma, resumen y actúan sobre el DOM.
- **MCP (Model Context Protocol)**: Probablemente están explorando o usando protocolos que permiten a los LLMs ver el DOM de la web de forma estructurada.
- **Agentic Retail (UCP)**: El nuevo **Universal Commerce Protocol** para que los agentes gestionen todo el funnel, desde el descubrimiento hasta el checkout automático en 2026.

## 2. Áreas de Contribución (Qué puedes aportar tú)

Dada tu experiencia y el rol, estas son las "medallas" que te puedes colgar en la entrevista:

1.  **Reliability (Fiabilidad)**: *"Puedo ayudar a diseñar sistemas de 'Evals' (evaluación) para asegurar que los agentes no se salgan del raíl en casos de borde (edge cases)."*
2.  **Latency (Latencia)**: En agentes de voz y realtime, cada milisegundo cuenta. Hablar de optimización de pipelines de audio y streaming de tokens es clave.
3.  **Context Engineering**: Gestión de ventanas de contexto largas sin perder precisión.
4.  **Integration Patterns**: Cómo escalar la conexión de agentes con decenas de CRMs distintos de forma genérica.

## 3. Roadmap de Formación (En qué hincar el codo)

Para ser el candidato perfecto, enfócate en estas 3 tecnologías:

### Nivel 1: PydanticAI (Imprescindible)
- **Por qué**: Es su estándar para agentes productivos.
- **Qué aprender**: Injection de dependencias en agentes, validación de modelos intermedios y `model_agnostic` tools.

### Nivel 2: OpenAI Realtime API & Voz
- **Por qué**: Es el núcleo de su proyecto de "Onboarding Automático".
- **Qué aprender**: Manejo de WebSockets para audio, interrupciones de voz (VAD) y reducción de latencia.

### Nivel 3: Go (Golang) para Backends de IA
- **Por qué**: Visión de futuro de Víctor Mollá.
- **Qué aprender**: Concurrencia (Goroutines) aplicada a llamadas paralelas de agentes y la librería `ollama` para Go o similares.

### Nivel 4: Observabilidad de LLMs
- **Formación**: Aprende qué son **LangSmith** o **Arize Phoenix**. En GuruSup necesitan saber *por qué* un agente falló a las 3 AM.
