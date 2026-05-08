import cv2
import numpy as np
import pytest

from lab5_metrics.services.metrics_service import analizar, generar_histograma


def test_analizar_reads_image_and_returns_metrics(tmp_path):
    image_path = tmp_path / "sample.png"
    image = np.array([[0, 50], [100, 150]], dtype=np.uint8)
    cv2.imwrite(str(image_path), image)

    result = analizar(str(image_path))

    assert result["mean"] == pytest.approx(75.0)
    assert result["min"] == 0
    assert result["max"] == 150


def test_analizar_rejects_invalid_image(tmp_path):
    invalid_path = tmp_path / "invalid.txt"
    invalid_path.write_text("no es una imagen")

    with pytest.raises(ValueError, match="No se pudo leer la imagen"):
        analizar(str(invalid_path))


def test_generar_histograma_creates_output_file(tmp_path):
    image_path = tmp_path / "sample.png"
    output_path = tmp_path / "charts" / "histograma.png"
    image = np.array([[0, 50], [100, 150]], dtype=np.uint8)
    cv2.imwrite(str(image_path), image)

    result = generar_histograma(str(image_path), str(output_path))

    assert result == str(output_path)
    assert output_path.exists()


def test_generar_histograma_rejects_invalid_image(tmp_path):
    invalid_path = tmp_path / "invalid.txt"
    invalid_path.write_text("no es una imagen")

    with pytest.raises(ValueError, match="No se pudo leer la imagen"):
        generar_histograma(str(invalid_path), str(tmp_path / "histograma.png"))
