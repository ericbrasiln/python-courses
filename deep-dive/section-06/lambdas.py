def sq(x):
    return x**2

print(type(sq))

lambda x: x**2

f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)

f(1, 'a','b',y=100,a=10,b=20)

def apply_func(x, fn):
    return fn(x)

apply_func(2, sq)

apply_func(2, lambda x: x**2)

apply_func(2, lambda x: x**3)

def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)

apply_func(sq, 3)

apply_func(lambda x: x**2, 3)

apply_func(lambda x, y: x+y, 1, 2)