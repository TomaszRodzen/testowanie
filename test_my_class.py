import math

import pytest

import my_class


def test_dog_initialization():
    d = my_class.Dog('Azor')
    assert d.name == 'Azor'


def test_dog_speak():
    d = my_class.Dog('Azor')
    assert d.speak() == 'hau-hau. Jestem Azor'


def test_lamp_initialization_off():
    l = my_class.Lamp(False)
    assert l.is_lightening() == False


def test_lamp_initialization_on():
    l = my_class.Lamp(True)
    assert l.is_lightening() == True


@pytest.fixture
def c():
    print('tworze obiekt kalkulatora')
    calc = my_class.Calc()
    return calc


@pytest.mark.parametrize('num1, num2, res',
                         [
                           (5, 10, 15),
                           (0, 0, 0),
                           (-3, -7, -10),
                           ('ab', 'cd', 'abcd'),
                           ('', '', '')
                         ])
def test_add_int(num1, num2, res, c):
    assert c.add(num1, num2) == res


def test_add_float(c):
    assert pytest.approx(c.add(3.2, 4.7), 0.01) == 7.9
    assert pytest.approx(c.add(1.1, -7.7), 0.01) == -6.6


def test_add_string(c):
    assert c.add('ab', 'cd') == 'abcd'


def test_circle_area():
    assert pytest.approx(my_class.circle_area(1), 0.001) == math.pi
    assert my_class.circle_area(0) == 0
    assert pytest.approx(my_class.circle_area(2.1), 0.001) == math.pi*(2.1**2)


def test_area_value_exceptions():
    with pytest.raises(ValueError):
        my_class.circle_area(-3)


def test_area_type_exception():
    with pytest.raises(TypeError):
        my_class.circle_area(True)


"""praca domowa. Stworzyc klase i ja przetestowac"""