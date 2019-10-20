import math


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'hau-hau. Jestem {self.name}'

    def rename(self, new_name):
        self.name = new_name


class Lamp:
    def __init__(self, light=False):
        self.light = light

    def turn_on(self):
        self.light = True

    def turn_off(self):
        self.light = False

    def is_lightening(self):
        return self.light


class Calc:

    def add(self, x, y):
        return x + y


def circle_area(r):
    if type(r) not in [float, int]:
        raise TypeError('the radius must be a number')
    if r < 0:
        raise ValueError('the radius cannot be negative')

    return math.pi*(r**2)


print(circle_area(2.2))