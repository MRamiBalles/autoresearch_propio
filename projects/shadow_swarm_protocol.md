# Protocolo de Operación: Shadow Swarm (Enjambres de Laboratorios Fantasma)

## 1. Arquitectura de Sincronización SQS (Sovereignty Quality Swarm)

Para escalar la investigación agéntica sin depender de clusters de GPUs, el sistema utiliza un modelo de **Sincronización Asíncrona vía Git-Flow**:

- **Nodo Maestro (Sovereign Core)**: Estación principal del usuario (actual).
- **Nodos Fantasma (Shadow Nodes)**: Estaciones de trabajo CPU distribuidas (ej: PCs de laboratorio, hardware doméstico).

## 2. Configuración de Ramas por Dominio

Cada nodo opera en una rama específica para evitar conflictos de escritura en los `results.tsv` locales:
- `swarm/medical/node-01`
- `swarm/materials/node-02`
- `swarm/llm/node-03`

## 3. Protocolo de Consolidación (Analyst Role)

1. **Exploración**: Cada nodo ejecuta ciclos de 4h-48h autónomos.
2. **Push de Resultados**: Los nodos suben sus `results.tsv` y `train.py` optimizados a sus ramas.
3. **Merge de Conocimiento**: El Agente `Analyst` en el Nodo Maestro realiza merges periódicos, integrando los mejores hiperparámetros de todos los laboratorios fantasma en la rama `master_sovereign`.

## 4. Instrucciones para Nuevos Nodos
```bash
git clone https://github.com/MRamiBalles/autoresearch_propio.git
git checkout -b swarm/<dominio>/node-<id>
$env:RESEARCH_MODE='<medical/materials/llm>'; python train.py --num-iterations 5000
```
