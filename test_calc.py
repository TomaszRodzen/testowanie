from calc import Calc


def test_add_two_numbers():
    c = Calc()
    assert c.add(4, 5) == 9


def test_add_thee_numbers():
    c = Calc()
    assert c.add(4, 5, 6) == 15


def test_add_five_numbers():
    c = Calc()
    assert c.add(4, 5, 7, 8)


def test_subtrackt_two_number():
    c = Calc()
    assert c.sub(10, 3) == 7


def test_multiply_two_numbers():
    c = Calc()
    assert c.mul(5, 2) == 10


def test_multiply_many_numbers():
    c = Calc()
    assert c.mul(1, 2, 3, 4, 5) == 120


def test_divide_two_numbers():
    c = Calc()
    assert c.divide(13, 2) == 6.5


def test_divide_by_zero():
    c = Calc()
    assert c.divide(7, 0) == 'inf'

