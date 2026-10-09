# Funciones del programa
import os

def guardar(H, flow, evp, dbrix, estado):
    archivo = 'reporte_turno.csv'
    existe = os.path.exists(archivo)
    with open(archivo, 'a', encoding='utf-8') as arch:
        if not existe:
            arch.write('Hora,Flujo,Agua_Evaporada,Delta_Brix,Estado_Alarma\n')
        arch.write(f'{H},{flow},{evp:.2f},{dbrix:.2f},{estado}\n')

def evaporacion(flow, b_in, b_out):
    '''
    Ecuacion para calcular la evaporacion en un evaporador
    con un balance simple
    '''
    if not (0 < b_in < b_out <= 100):
        raise ValueError("Se requiere 0 < Brix_in < Brix_out <= 100")
    return flow * (1 - b_in / b_out)
