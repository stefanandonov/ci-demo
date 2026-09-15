from calculator import add, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(5, 3) == 8


def test_subtract():
    assert subtract(10, 4) == 6
