from __future__ import annotations

from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray


class ImageMetrics:
    def calcular_metricas(self, imagen: NDArray[Any]) -> dict[str, float | int]:
        return {
            "mean": float(np.mean(imagen)),
            "std": float(np.std(imagen)),
            "min": int(np.min(imagen)),
            "max": int(np.max(imagen)),
        }

    def guardar_histograma(self, imagen: NDArray[Any], output_path: str) -> str:
        plt.figure()
        plt.hist(imagen.flatten(), bins=50)
        plt.title("Histograma")
        plt.xlabel("Intensidad")
        plt.ylabel("Frecuencia")
        plt.savefig(output_path)
        plt.close()
        return output_path
