# Soft sensor de evaporador

Proyecto de aprendizaje aplicado para el monitoreo y la estimación de variables de una corrida de evaporación de múltiple efecto en la industria azucarera.

> Aviso: todos los datos de este repositorio son sintéticos y no corresponden a una planta real.

## Descripción general

Este proyecto modela el comportamiento de un evaporador mediante un balance de sólidos y una lógica de clasificación operativa. La aplicación toma lecturas horarias, calcula la cantidad de agua evaporada, evalúa la variación del Brix y determina si el equipo se encuentra en estado óptimo, baja eficiencia, detenido o con sensor defectuoso.

## Integraciones actuales

El sistema ya incluye las siguientes integraciones y componentes:

- Python 3.10+ como motor principal del análisis
- SQLite como base de datos local para persistencia de lecturas y resultados
- Pandas para lectura, transformación y agregación de series temporales
- SciPy como base para análisis numérico y cálculo asociado a la evaporación
- pytest para validación de lógica y regresión
- Generación de datos sintéticos para pruebas y simulación del proceso

## Arquitectura funcional

El flujo del proyecto es el siguiente:

1. Carga de datos de entrada (flujo, Brix de entrada/salida y estado de la válvula)
2. Cálculo del agua evaporada mediante el balance de sólidos
3. Clasificación del estado operativo del equipo
4. Persistencia de lecturas y resultados en SQLite
5. Generación de reportes agregados por series temporales

### Balance de sólidos

W = F · (1 − Brix_in / Brix_out)

Donde:
- F: flujo de alimentación (t/h)
- Brix_in: concentración de entrada
- Brix_out: concentración de salida
- W: agua evaporada (t/h)

## Base de datos

La persistencia se realiza con SQLite mediante las tablas:

- `efecto`: identifica los equipos o vasos
- `historial_efecto`: almacena lecturas históricas
- `resultados_efecto`: guarda resultados calculados por lectura

Esto permite mantener un histórico de operación y facilitar análisis posteriores sin depender de un motor externo.

## Estructura del proyecto

```text
.
├── config/
│   └── constant.py        # configuración y rutas de la base de datos
├── src/
│   ├── alarma.py           # clasificación de estados operativos
│   ├── db.py               # conexión, inserción y extracción desde SQLite
│   ├── evaporador.py       # lógica del balance y cálculo del EPE
│   ├── reporte.py          # agregación y resumen temporal
│   ├── models/
│   │   ├── lecturas.py     # datos sintéticos de ejemplo
│   │   └── evaporador.db   # base de datos local
│   └── tests/
│       └── test_evaporador.py
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Estado del proyecto

- [x] Fase I: fundamentos (balance de evaporación, alarmas, registro CSV/SQLite)
- [x] Fase II: SQL, Pandas y series temporales
- [ ] Fase III: modelo físico y generación de datos sintéticos
- [ ] Fase IV: modelo híbrido y validación

## Cómo ejecutarlo

### 1) Clonar el repositorio

```bash
git clone https://github.com/RommelVargas/soft-sensor-evaporador.git
cd soft-sensor-evaporador
```

### 2) Instalar dependencias

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
pip install pandas scipy pytest
```

### 3) Ejecutar la aplicación

```bash
python main.py
```

La ejecución crea o actualiza la base de datos SQLite y genera los resultados del análisis del equipo.

## Pruebas

```bash
python -m pytest -v
```

## Casos de uso

- Monitoreo de desempeño de un evaporador
- Detección de estado operativo anómalo
- Evaluación de pérdida de eficiencia por reducción de ΔBrix
- Registro histórico para análisis posterior del proceso

## Limitaciones actuales

- Modelo de balance simple, sin elevación del punto de ebullición detallada ni coeficiente de transferencia completo
- Alarmas con umbrales fijos para la variación del Brix
- Base de datos local, pensada para uso de laboratorio y aprendizaje

## Licencia

MIT
