import cv2
import numpy as np
import pytest
from fastapi.testclient import TestClient

from lab5_metrics.api import main


def test_analyze_metrics_endpoint_returns_image_metrics(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "DATA_DIR", tmp_path / "data")
    image_path = tmp_path / "api-sample.png"
    image = np.array([[10, 20], [30, 40]], dtype=np.uint8)
    cv2.imwrite(str(image_path), image)
    client = TestClient(main.app)

    with image_path.open("rb") as image_file:
        response = client.post(
            "/analyze-metrics",
            files={"file": ("api-sample.png", image_file, "image/png")},
        )

    assert response.status_code == 200
    assert response.json()["mean"] == pytest.approx(25.0)


def test_analyze_metrics_endpoint_rejects_invalid_image(tmp_path, monkeypatch):
    monkeypatch.setattr(main, "DATA_DIR", tmp_path / "data")
    invalid_path = tmp_path / "invalid.txt"
    invalid_path.write_text("no es una imagen")
    client = TestClient(main.app)

    with invalid_path.open("rb") as invalid_file:
        response = client.post(
            "/analyze-metrics",
            files={"file": ("invalid.txt", invalid_file, "text/plain")},
        )

    assert response.status_code == 400
    assert "No se pudo leer la imagen" in response.json()["detail"]
