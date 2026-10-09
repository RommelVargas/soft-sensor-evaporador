# Soft sensor de evaporador

Proyecto de aprendizaje aplicado: monitoreo y estimación de variables de una
estación de evaporación de múltiple efecto (industria azucarera), con Python,
SQL, SciPy y validación sobre series temporales.

> **Aviso:** todos los datos de este repositorio son **sintéticos**.
> No se usa información de ninguna planta real.

## Estado

- [x] Fase I: fundamentos (balance de evaporación, alarmas, registro CSV)
- [ ] Fase II: SQL, Pandas y series temporales
- [ ] Fase III: modelo físico y generación de datos sintéticos
- [ ] Fase IV: modelo híbrido y validación

## Qué hace hoy (Fase I)

Recorre lecturas horarias de un evaporador (flujo de entrada, Brix de entrada
y salida, estado de la válvula de vapor), calcula el agua evaporada y asigna
un estado: equipo detenido, sensor en mal estado, baja eficiencia u óptimo.
Guarda los resultados en `reporte_turno.csv`.

Balance de sólidos usado:

    W = F · (1 − Brix_in / Brix_out)

donde `F` es el flujo de entrada (t/h) y `W` el agua evaporada (t/h).

## Cómo ejecutarlo

```bash
git clone https://github.com/RommelVargas/soft-sensor-evaporador.git
cd soft-sensor-evaporador
python main.py
```

Se necesita Python 3.10 o superior. Cada ejecución añade filas al CSV
(modo *append*).

## Pruebas

```bash
pip install pytest
python -m pytest -v
```

## Estructura

    evaporador.py   # funciones: evaporacion(), guardar()
    main.py         # programa principal con lecturas de ejemplo
    tests/          # pruebas con pytest

## Limitaciones

- Modelo de balance simple, sin elevación del punto de ebullición ni
  coeficiente de transferencia (se incorporan en la Fase III).
- Las alarmas usan un umbral fijo de ΔBrix.

## Licencia

MIT
