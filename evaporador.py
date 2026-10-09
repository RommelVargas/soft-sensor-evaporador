# Funciones del programa
import os

# Funcion de guardar en csv
def guardar(Hora, flow, agua_evaporada, dbrix, estado_alarma):
    archivo = 'reporte_turno.csv'
    existe = os.path.exists(archivo)
    with open(archivo, 'a', encoding='utf-8') as arch:
        if not existe:
            arch.write('Hora,Flujo,Agua_Evaporada,Delta_Brix,Estado_Alarma\n')
        arch.write(f'{Hora},{flow},{agua_evaporada:.2f},{dbrix:.2f},{estado_alarma}\n')

# funcion para calcular la cantidad de agua que pierde el jugo
def evaporacion(flow, b_in, b_out):
    '''
        Ecuacion para calcular la evaporacion en un evaporador
        con un balance simple
        W = F - L
        F * xf = L * xl
        W = F * (1 - (xf/xl))
    '''
    # Comprobacion
    if not (0 < b_in < b_out <= 100):
        raise ValueError("Se requiere 0 < Brix_in < Brix_out <= 100")
    return flow * (1 - b_in / b_out)
