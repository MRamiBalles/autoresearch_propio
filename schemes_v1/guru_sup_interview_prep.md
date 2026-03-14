# GuruSup Interview Preparation Guide (Software Engineer - LLMs & GenAI)

Este documento es una hoja de ruta estratégica diseñada para Manuel, estructurada para demostrar un conocimiento profundo de la empresa y una alineación técnica total con su visión de "Agentic Engineering".

## 1. Contexto Estratégico y Empresa

### El Fundador: Víctor Mollá (no Victoriano Izquierdo)
> [!IMPORTANT]
> Es vital no confundir a **Víctor Mollá** (Founder/CEO de GuruSup) con Victoriano Izquierdo (CEO de Graphext). Víctor Mollá fue una figura clave en **GuruWalk** antes de lanzar GuruSup. Esto explica por qué te escribe Bruno desde un correo de GuruWalk: son parte del mismo ecosistema de talento en Valencia.

### El Pivot: De soporte a automatización interna
GuruSup no es ya una simple herramienta de "Customer Support". Están evolucionando hacia un sistema de **orquestación de procesos internos**.
- **Salespath**: Su producto para ventas B2B que utiliza agentes para prospección e inteligencia comercial.
- **Visión**: Crear "empleados digitales" que vivan en el stack de la empresa (CRM, WhatsApp, Slack).

## 2. Definición Técnica: El Stack GuruSup

### Agentic Engineering & PydanticAI (v1.67.0+)
GuruSup no solo usa LLMs; están construyendo frameworks de agentes.
- **PydanticAI v1.67.0**: Menciona el soporte para **GPT-5.4** y el nuevo **WebSearchTool** para OpenRouter. Esto demuestra que estás al día con los lanzamientos de la última semana.
- **Vibe Coding / AI-Native**: Programan *usando* IA. Esperan que seas experto en Cursor, Claude Code y en orquestar agentes para escribir código (no solo escribirlo tú solo).

### El futuro en Go (Golang)
Víctor Mollá ha defendido recientemente que **Go** será fundamental para el backend de IA.
- **Razón**: El tipado fuerte y los errores descriptivos ayudan a que los propios agentes de IA (los que programan) entiendan por qué algo falló y lo arreglen solos.

### Frontend e Interacción
- **Voz y Realtime**: Uso de la API Realtime de OpenAI y avatares para onboardings (proyecto "Ana").
- **Browser Automation**: Interés real en agentes que naveguen por la web (Playwright).

## 3. Estrategia para la Entrevista (45 min con Bruno)

### Temas clave a mencionar:
1. **Orquestación sobre Prompting**: Demuestra que te interesa cómo conectar agentes, no solo cómo escribir un prompt largo.
2. **Confiabilidad (Reliability)**: Habla de evaluaciones (Evals) y cómo usas Pydantic para que la IA no alucine en producción.
3. **Velocidad de ejecución**: En GuruSup valoran el "Shipping" rápido.

### Preguntas "Ganadoras" para hacerles:
- *"He visto que estáis explorando Go para el backend de agentes por su capacidad de auto-corrección. ¿En qué punto de esa migración os encontráis?"*
- *"Tras el éxito de Salespath, ¿cuál es el siguiente proceso interno que veis más maduro para ser 'agentalizado'?"*
- *"¿Cómo gestionáis la observabilidad de los agentes en el AI Night Lab para asegurar que el comportamiento en producción es el esperado?"*

## 4. Plan de Acción Inmediato
- [ ] Revisar la documentación de **PydanticAI v1.67.0** (WebSearchTool & GPT-5.4 readiness).
- [ ] Investigar sobre **Agentic Retail (UCP)**: Cómo los agentes controlarán el checkout completo en 2026.
- [ ] Escuchar el episodio de Víctor Mollá en el podcast **"El Test de Turing"** (si no lo has hecho ya).
- [ ] Preparar ejemplos de cómo has usado **agentes de navegación** o automatización de procesos internos.
