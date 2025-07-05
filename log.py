"""
Configuración del logger para el proyecto.
"""

import os
import logging
import datetime

from config.rutas import DIR_LOGS
from config.constantes import PATRON_LOGS, LIMITE_LOGS

os.makedirs(DIR_LOGS, exist_ok=True)

archivos = [
    os.path.join(DIR_LOGS, archivo)
    for archivo in os.listdir(DIR_LOGS)
    if PATRON_LOGS.match(archivo)
]

archivos.sort(key=os.path.getctime, reverse=True)
while len(archivos) > LIMITE_LOGS:
    archivo_a_borrar = archivos.pop()
    try:
        os.remove(archivo_a_borrar)
    except Exception as e:
        print(f"No se pudo borrar '{archivo_a_borrar}': {e}")

fecha_actual = datetime.datetime.now().strftime('%d-%m-%Y')
archivo_log = os.path.join(DIR_LOGS, f"log_{fecha_actual}.txt")

if not logging.getLogger().hasHandlers():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] (%(levelname)s) %(message)s',
        datefmt='%H:%M:%S',
        handlers=[
            logging.FileHandler(archivo_log, mode="a", encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

logger = logging.getLogger(__name__)
