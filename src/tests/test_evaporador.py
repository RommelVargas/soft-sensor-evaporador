import pytest
from evaporador import evaporacion

def test_balance_basico():
    # 250 t/h, Brix 15 -> 22.5  =>  250 * (1 - 15/22.5) = 83.33
    assert evaporacion(250.0, 15.0, 22.5) == pytest.approx(83.33, abs=0.01)

def test_brix_salida_cero():
    with pytest.raises(ValueError):
        evaporacion(250.0, 15.0, 0.0)

def test_brix_salida_menor_que_entrada():
    with pytest.raises(ValueError):
        evaporacion(250.0, 15.0, 10.0)
