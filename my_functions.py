def add(x, y):
    """Add function"""
    return x + y


def substract(x, y):
    """substract function"""
    return x - y


def multiply(x, y):
    """Multiply function"""
    return x * y


def divide(x, y):
    """Divide function"""
    if y == 0:
        raise ValueError('cannot divide by zero')
    return x / y


def square(x):
    """return square root of the given argument"""
    if x < 0:
        raise ValueError('Cannot square the negative number')
    return x ** 0.5