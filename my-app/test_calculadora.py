import pytest
from calculadora import soma, subtrai, multiplica, divide

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, -2) == -3
    assert soma(0, 0) == 0

def test_subtrai():
    assert subtrai(5, 3) == 2
    assert subtrai(-5, -3) == -2
    assert subtrai(0, 5) == -5

def test_multiplica():
    assert multiplica(2, 3) == 6
    assert multiplica(-2, 3) == -6
    assert multiplica(0, 100) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 2) == 4.5
    assert divide(0, 1) == 0

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)