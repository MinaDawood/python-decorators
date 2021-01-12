def pfib(a, b, c):
    print(a, b, c)

pfib(1, 2, 3)

def pfib2(a, *args):
    print(a)
    print(args)

pfib2(1, 2, 3,4)

def pfib3(a, **kwargs):
    print(a)
    print(kwargs)

pfib3(1, se=1, th=2, fo=3, fi=5)

def pfib4(*args, **kwargs):
    print(args)
    print(kwargs)

pfib4(1, 1, 2, fo=4, fi=5)