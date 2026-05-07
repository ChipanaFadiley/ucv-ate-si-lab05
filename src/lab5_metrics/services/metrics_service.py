from __future__ import annotations

from pathlib import Path

import cv2

from lab5_metrics.analyzer import ImageMetrics


def analizar(path: str) -> dict[str, float | int]:
    imagen = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        raise ValueError(f"No se pudo leer la imagen: {path}")

    analyzer = ImageMetrics()
    return analyzer.calcular_metricas(imagen)


def generar_histograma(path: str, output_path: str) -> str:
    imagen = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if imagen is None:
        raise ValueError(f"No se pudo leer la imagen: {path}")

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    analyzer = ImageMetrics()
    return analyzer.guardar_histograma(imagen, output_path)
