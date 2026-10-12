from src.models.lecturas import *
from src.reporte import *
from src.alarma import *
from src.db import *

if __name__ == "__main__":
    crear()
    ingresar(name, datos)
    df = extraer()
    for id, flujo, b_in, b_out, abierta in df:
        agua_ret, dbrix, estado, epe = clasificar(flujo, b_in, b_out, abierta)
        guardar(id, dbrix, agua_ret, estado, epe)
    print('Analisis del brix de salida y la elvacion del punto de ebuccion en el tuno')
    print(reporte())
