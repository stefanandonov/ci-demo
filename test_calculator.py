from calculator import add, subtract, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(5, 9) == 45
