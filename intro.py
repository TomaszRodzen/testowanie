def div(a, b):
    return (a+b)**2


if __name__ == '__main__':
    assert div(2, 2) == 16, 'Failed'
    print('first test: passed')
    assert div(5, 6) == 121, 'Failed'
    print('second test: passed')
    assert div(3, 2) == 25, 'Failed'
    print('third test: passed')

