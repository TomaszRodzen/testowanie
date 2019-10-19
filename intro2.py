def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


assert factorial(5) == 120, 'Failed'
assert factorial(4) == 24, 'Failed'

print(factorial(5))
print(factorial(4))