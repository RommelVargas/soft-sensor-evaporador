from evaporador import guardar, evaporacion

# lecturas de ejemplo
lecturas = [
# [Hora, Flujo_in (ton/h), Brix_in, Brix_out, Valvula_Vapor_Abierta]
    ["22:00", 250.0, 15.0, 22.5, True],
    ["23:00", 252.1, 14.9, 22.8, True],
    ["00:00", 248.5, 15.1, 18.6, True],
    ["01:00", 250.0, 15.0, 22.4, True],
    ["02:00", 0.0, 0.0, 0.0, False],
    ["03:00", 255.0, 15.2, 0.0, True],
    ["04:00", 251.5, 15.0, 22.6, True],
    ["05:00", 250.0, 14.8, 22.1, True]
]

if __name__ == "__main__":
    for hora, flujo, b_in, b_out, abierta in lecturas:
        agua_ret = 0.0
        dbrix = b_out - b_in
        umbral = 5
        if not abierta:
            estado = "Equipo detenido."
        elif b_out <= 0:
            estado = 'Sensor en mal estado!'
            dbrix = 0
        elif abierta and dbrix < umbral:
            try:
                agua_ret = evaporacion(flujo, b_in, b_out)
                estado = "Baja eficiencia de evaporación.!"
            except ValueError:
                raise ValueError('Dato inconsistente')
        else:
            try:
                estado = 'Optimo'
                agua_ret = evaporacion(flujo, b_in, b_out)
            except ValueError:
                raise ValueError('Dato inconsistente')
        guardar(hora, flujo, agua_ret, dbrix, estado)
