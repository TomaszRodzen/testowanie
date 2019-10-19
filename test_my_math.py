import my_math


def test_add():
    assert my_math.add(7, 3) == 10
    assert my_math.add(7, -1) == 6
    assert my_math.add(4.3, 5.3) == 9.6


def test_multiply():
    assert my_math.multiply(3, 4) == 12
    assert my_math.multiply(5, 2) == 10
    assert my_math.multiply(7, 6) == 42


def test_string_reverse():
    assert my_math.string_reverse('word') == 'drow'
    assert my_math.string_reverse('second') == 'dnoces'


def test_square():
    assert my_math.square(2) == 4
    assert my_math.square(3) == 9
    assert my_math.square(9) == 81


test_square()
test_add()
test_multiply()
test_string_reverse()
