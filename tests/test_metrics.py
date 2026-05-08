import numpy as np
import pytest

from lab5_metrics.analyzer import ImageMetrics


def test_metrics_for_zero_image():
    img = np.zeros((10, 10))
    analyzer = ImageMetrics()
    result = analyzer.calcular_metricas(img)

    assert result["mean"] == pytest.approx(0.0)
    assert result["std"] == pytest.approx(0.0)
    assert result["min"] == 0
    assert result["max"] == 0


def test_metrics_for_mixed_image():
    img = np.array([[0, 10], [20, 30]])
    analyzer = ImageMetrics()
    result = analyzer.calcular_metricas(img)

    assert result["mean"] == pytest.approx(15.0)
    assert result["min"] == 0
    assert result["max"] == 30


def test_guardar_histograma_creates_file(tmp_path):
    img = np.array([[0, 10], [20, 30]])
    output_path = tmp_path / "histograma.png"
    analyzer = ImageMetrics()

    result = analyzer.guardar_histograma(img, str(output_path))

    assert result == str(output_path)
    assert output_path.exists()
