"""
Módulo de configuración de rutas para el proyecto.
"""

from pathlib import Path

DIR_BASE = Path(__file__).resolve().parent.parent
DIR_TESTS = DIR_BASE / 'tests'
DIR_TEST_RECURSOS = DIR_TESTS / "recursos"
