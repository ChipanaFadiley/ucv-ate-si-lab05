from __future__ import annotations

import shutil
from pathlib import Path

from fastapi import FastAPI, HTTPException, UploadFile

from lab5_metrics.services.metrics_service import analizar

app = FastAPI(title="Lab 5 Metrics API")

DATA_DIR = Path("data")


@app.post("/analyze-metrics")
def analyze(file: UploadFile) -> dict[str, float | int]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    filename = Path(file.filename or "imagen").name
    path = DATA_DIR / filename

    with path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        return analizar(str(path))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
