from config.constant import *
import sqlite3
import pandas as pd

# Base proviene de la carpeta de configuraciones el cual equivale a evaporador.d

def crear():
    conexion = sqlite3.connect(DB_PATH)
    try:
        cursor = conexion.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS efecto(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            efecto TEXT NOT NULL UNIQUE
            )
            ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS historial_efecto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                efecto_id INTEGER,
                fecha_hora DATETIME NOT NULL,
                flujo_alimentacion REAL,
                brix_entrada REAL,
                brix_salida REAL,
                valvula BOOLEAN,
                FOREIGN KEY (efecto_id) REFERENCES efecto(id),
                UNIQUE(efecto_id, fecha_hora)
            )
            ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resultados_efecto (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 lectura_id INTEGER,
                 delta_brix REAL,
                 agua_evaporada REAL,
                 estado_operativo TEXT,
                 epe REAL,
                 FOREIGN KEY (lectura_id) REFERENCES historial_efecto(id)
                )
            ''')
    finally:
        conexion.close()


def ingresar(name, datos):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    sql_efectos = '''
        INSERT OR IGNORE INTO efecto (efecto)
        VALUES (?)
    '''
    sql_lecturas = '''
        INSERT OR IGNORE INTO historial_efecto (efecto_id, fecha_hora, flujo_alimentacion, brix_entrada, brix_salida, valvula)
        VALUES (?, ?, ?, ?, ?, ?)
        '''
    try:
        cursor.executemany(sql_efectos, name)
        conexion.commit()
        cursor.executemany(sql_lecturas, datos)
        conexion.commit()
    finally:
        conexion.close()

def extraer():
    conexion = sqlite3.connect(DB_PATH)
    peticion = '''
    SELECT id, flujo_alimentacion, brix_entrada, brix_salida, valvula
    FROM historial_efecto
    '''
    try:
        df = pd.read_sql_query(peticion, conexion)
        return list(df.itertuples(index=False, name=None))
    finally:
        conexion.close()


# Funcion de guardar en sql
def guardar(lectura_id, dbrix, agua_evaporada, estado_alarma, epe):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    variables = (lectura_id, dbrix, agua_evaporada, estado_alarma, epe)
    ingresar = '''
        INSERT INTO resultados_efecto (
            lectura_id,
            delta_brix,
            agua_evaporada,
            estado_operativo,
            epe
        ) VALUES (?, ?, ?, ?, ?)
    '''
    try:
        cursor.execute(ingresar, variables)
        conexion.commit()
    finally:
        conexion.close()
