def func(a, b, *args, **kwargs):
    print('a: ', a)
    print('b: ', b)
    print('args: ', args)
    print('kwargs: ', kwargs)


func(1, 2, 3, x=5, ala=10)
