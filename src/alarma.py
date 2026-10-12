from .evaporador import *

UMBRAL_DBRIX = 5
def clasificar(flujo, b_in, b_out, abierta):
    if not abierta:
        return 0.0, 0.0, "Equipo detenido.", 0.0
    if b_out <= 0:
        return 0.0, 0.0, "Sensor en mal estado.", 0.0
    try:
        agua = evaporacion(flujo, b_in, b_out)
        elevacion = epe(b_out)
    except ValueError:
        return 0.0, 0.0, "Datos inconsistentes.", 0.0
    dbrix = b_out - b_in
    estado = "Baja eficiencia." if dbrix < UMBRAL_DBRIX else "Optimo"
    return agua, dbrix, estado, elevacion
