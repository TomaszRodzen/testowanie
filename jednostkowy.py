def add(x, y):
    return x + y


def test_add():
    assert add(7, 3) == 10
    assert add(7, -1) == 6
    assert add(4.3, 5.3) == 9.6


def multiply(a, b):
    return a * b


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(5, 2) == 10
    assert multiply(7, 6) == 42


test_add()
test_multiply()
