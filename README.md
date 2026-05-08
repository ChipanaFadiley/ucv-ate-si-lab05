# Laboratorio 05 - Metricas de imagenes via API

Sistema de analisis estadistico de imagenes que calcula metricas basicas y expone los resultados mediante una API con FastAPI.

## Requisitos

- Python 3.11 o superior
- Poetry
- PowerShell

## Instalacion

```powershell
poetry config virtualenvs.in-project true
poetry install
```

## Ejecucion de la API

```powershell
poetry run uvicorn lab5_metrics.api.main:app --reload
```

Endpoint disponible:

- `POST /analyze-metrics`

Ejemplo con PowerShell:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/analyze-metrics" `
  -Method Post `
  -Form @{ file = Get-Item ".\ruta\a\imagen.png" }
```

Respuesta esperada:

```json
{
  "mean": 0.0,
  "std": 0.0,
  "min": 0,
  "max": 0
}
```

## Pruebas y cobertura

```powershell
poetry run pytest
```

El comando genera `coverage.xml`, que queda referenciado en `sonar-project.properties`.

## SonarQube Cloud con GitHub Actions

El proyecto esta preparado para analizarse automaticamente desde GitHub Actions.

1. Crear el repositorio en GitHub:

```text
ChipanaFadiley/ucv-ate-si-lab05
```

2. Crear/importar el proyecto en SonarQube Cloud con estos datos:

- Organization key: `chipanaadiley`
- Project key: `ChipanaFadiley_ucv-ate-si-lab05`
- Project name: `ucv-ate-si-lab05`

3. Crear un token en SonarQube Cloud desde `Account > Security`.
   Nombre recomendado del token:

```text
sonar-token-lab05
```

4. Guardar ese token en GitHub:
   `Settings > Secrets and variables > Actions > New repository secret`

```text
Name: SONAR_TOKEN
Value: token_generado_en_sonarqube_cloud
```

5. Subir cambios a `main`. GitHub Actions ejecutara:

- instalacion de dependencias
- pruebas con cobertura
- analisis de SonarQube Cloud

Tambien se puede ejecutar localmente:

```powershell
poetry run pytest
```
