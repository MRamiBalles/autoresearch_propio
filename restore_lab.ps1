# Autoresearch Lab Restoration Script (Native PowerShell)
Write-Host "--- Autoresearch Lab Restoration (Shadow Swarm) ---" -ForegroundColor Cyan

# 1. Limpieza de procesos previos
Write-Host "Limpiando procesos Python previos..."
$py_procs = Get-Process python -ErrorAction SilentlyContinue
if ($py_procs) { $py_procs | Stop-Process -Force }
Start-Sleep -s 3

# 2. Lanzamiento de Nodos
Write-Host "Lanzando hilos de investigación..."

# Master Long-Term (Medical)
Start-Process powershell -ArgumentList "-NoProfile", "-Command", "`$env:RESEARCH_MODE='medical'; python train.py --warmup-steps 100 >> research_long.log 2>&1" -WindowStyle Hidden

# Materials Node
Start-Process powershell -ArgumentList "-NoProfile", "-Command", "`$env:RESEARCH_MODE='materials'; python train.py --num-iterations 500 --warmup-steps 100 >> swarm_node_01-Materials.log 2>&1" -WindowStyle Hidden

# Medical Scout Node
Start-Process powershell -ArgumentList "-NoProfile", "-Command", "`$env:RESEARCH_MODE='medical'; python train.py --num-iterations 500 --warmup-steps 100 >> swarm_node_02-Medical-Scout.log 2>&1" -WindowStyle Hidden

# 3. Orquestador
Start-Process powershell -ArgumentList "-NoProfile", "-Command", "python shadow_swarm_orchestrator.py >> shadow_orchestrator.log 2>&1" -WindowStyle Hidden

Write-Host "[OK] Lab restaurado. Verifique 'swarm_status.md' en 60 segundos." -ForegroundColor Green
