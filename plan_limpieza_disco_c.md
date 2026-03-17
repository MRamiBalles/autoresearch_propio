# Plan de Limpieza y Recuperación de Espacio - Disco C:

## 1. Diagnóstico de Emergencia
El disco **C:** se encuentra con **0 bytes libres**. Esto bloquea el funcionamiento del sistema, la persistencia de logs y el rendimiento general. El disco **D:** dispone de **607 GB**, lo que ofrece una solución de migración ideal.

## 2. Candidatos Principales para Eliminación/Migración

| Ubicación | Contenido Estimado | Acción Sugerida |
| :--- | :--- | :--- |
| `C:\Users\Manu\.cache\autoresearch\data` | **Varios GB** de shards de datos (.parquet). | **Migrar a D:** o Borrar (se pueden descargar de nuevo si es necesario). |
| `C:\Users\Manu\.gemini\antigravity\brain` | **GigaBytes** de grabaciones y capturas de sesiones agénticas. | **Borrar sesiones antiguas**. Mantener solo la actual (`188a6956...`). |
| `C:\Users\Manu\AppData\Local\Temp` | Basura temporal del sistema. | **Borrado Seguro** (archivos no usados en las últimas 24h). |
| `C:\Users\Manu\Downloads` | Instaladores y archivos duplicados. | **Auditoría de Duplicados** (ej: archivos con `(1)`, `(2)`). |

## 3. Archivos Duplicados Detectados (Muestra)
He detectado patrones de duplicación (`* (1).exe`, `* - Copy.zip`) que suelen acumularse en `Downloads`. Recomiendo pasar estos archivos a D: si son necesarios, o borrarlos.

## 4. Estrategia de Soberanía a Largo Plazo
Para evitar que esto ocurra de nuevo, propongo reconfigurar el `CACHE_DIR` en nuestro código directamente hacia D:.
```python
# Propuesta para prepare.py / train.py
CACHE_DIR = "d:\\autoresearch\\.cache"
```

## 5. Instrucciones de Limpieza Manual (Recomendadas para ti)
1. **Vaciar Papelera de Reciclaje**.
2. **Eliminar contenido de**: `C:\Users\Manu\AppData\Local\Temp`.
3. **Eliminar carpetas de sesiones antiguas en**: `C:\Users\Manu\.gemini\antigravity\brain` (excepto la activa).
4. **Borrar la carpeta de datos de caché**: `C:\Users\Manu\.cache\autoresearch\data`.

**¿Procedo a automatizar el cambio de CACHE_DIR a D: en el código para que las nuevas descargas no llenen C:?**
