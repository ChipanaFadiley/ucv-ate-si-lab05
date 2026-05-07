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

## SonarQube / SonarCloud

1. Crear un proyecto en SonarQube o SonarCloud.
2. Crear un token desde `Account > Security > Generate Tokens`.
3. Guardar el token en PowerShell:

```powershell
$env:SONAR_TOKEN="tu_token"
```

4. Ejecutar las pruebas para generar cobertura:

```powershell
poetry run pytest
```

5. Ejecutar el scanner desde la raiz del repositorio:

```powershell
sonar-scanner -D"sonar.token=$env:SONAR_TOKEN"
```

Si SonarCloud pide organizacion o clave distinta, actualizar `sonar-project.properties` con los valores del proyecto creado.
