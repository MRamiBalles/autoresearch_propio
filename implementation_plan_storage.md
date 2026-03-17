# Plan de Saneamiento y Migración de Datos (Soberanía de Almacenamiento)

Este plan detalla las acciones para recuperar espacio en el disco **C:** (actualmente en 0B) y asegurar que el laboratorio `autoresearch` opere en el disco **D:** (607GB libres).

## Cambios Propuestos

### Infraestructura de Datos
*   **[MODIFY] [prepare.py](file:///d:/autoresearch/prepare.py)**: Cambiar `CACHE_DIR` para apuntar a `D:\autoresearch\.cache`.
*   **[MODIFY] [train.py](file:///d:/autoresearch/train.py)**: Cambiar `CACHE_DIR` para apuntar a `D:\autoresearch\.cache`.

### Limpieza de C:
*   **[DELETE]**: Carpeta `C:\Users\Manu\.cache\autoresearch\data`.
*   **[DELETE]**: Sesiones antiguas en `C:\Users\Manu\.gemini\antigravity\brain` (excepto la actual).

## Plan de Verificación

### Pruebas de Sistema
- Ejecutar `python prepare.py --num-shards 1` para verificar que la nueva caché se crea en D:.
- Verificar espacio libre en C: mediante `Get-PSDrive C`.

### Verificación Manual
- El usuario debe confirmar la eliminación de los archivos temporales y sesiones de Gemini.
