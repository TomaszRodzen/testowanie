class Calc:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        res = 1
        for item in args:
            res *= item
        return res

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'inf'
