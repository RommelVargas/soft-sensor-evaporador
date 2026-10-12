from pathlib import Path

# Base de datos
DB_PATH = Path(__file__).resolve().parent.parent / "src" / "models" / "evaporador.db"

# Contantes para calcular la elevacion del punto de ebullicion
c1 = 0.015 # ecuacion lineal
a, b, c = 0.1, 1.5e-3, -1.5e-5 # ecuacion polinomial
