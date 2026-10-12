from config.constant import DB_PATH
import pandas as pd
import sqlite3

def reporte():
    conexion = sqlite3.connect(DB_PATH)
    peticion = '''
        SELECT
            historial_efecto.fecha_hora,
            historial_efecto.brix_salida,
            resultados_efecto.epe
        FROM resultados_efecto
        JOIN historial_efecto ON resultados_efecto.lectura_id = historial_efecto.id
    '''
    df = pd.read_sql_query(peticion, conexion)
    df['fecha_hora'] = pd.to_datetime(df['fecha_hora'])
    df = df.set_index('fecha_hora').sort_index()

    df_hora = df.resample('2h').mean()
    df_hora['brix_salida'] = df_hora['brix_salida'].rolling(window=3, min_periods=1).mean()
    return df_hora
