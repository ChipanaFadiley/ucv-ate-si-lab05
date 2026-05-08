Laboratorio 5 de Sistemas Inteligentes - Metricas de imagenes y API

Descripcion
En este proyecto se desarrollo una API en Python usando FastAPI, OpenCV y NumPy.

La API permite subir una imagen, procesarla en escala de grises y calcular metricas basicas. Como resultado devuelve un JSON con:

media de intensidad
desviacion estandar
valor minimo
valor maximo

Estructura basica
src/lab5_metrics/api/main.py: API principal
src/lab5_metrics/services/metrics_service.py: lectura y procesamiento de imagen
src/lab5_metrics/analyzer.py: calculo de metricas e histograma
tests/test_api.py: pruebas de la API
tests/test_metrics.py: pruebas de metricas
tests/test_metrics_service.py: pruebas del servicio

Evidencias
docs/evidencias/imagenes: imagenes usadas para la prueba
docs/evidencias/histogramas: graficos generados con matplotlib
