from config.constant import *

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
    return round(flow * (1 - b_in / b_out), 2)

# Elevacion del punto de ebullicion
def epe(brix):
    '''
    Para temperatura en grados celsius
    para brix < 40 la opcion lineal
    para brix 40 - 85 la opcion polinomial
    '''
    if (brix<40):
        return round((c1 *brix), 2)
    return round((a * brix + b * brix ** 2 + c * brix **3),2)
