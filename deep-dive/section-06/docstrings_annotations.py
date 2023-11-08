def func(a: int,
         b: int) -> int:
    """
    This function return a * b.
    """
    return a * b

def my_func(a: str,
            b: 'int > 0' = 1,
            *args: 'some extra positional args',
            k1: 'keyword-only arg 1',
            k2: 'keyword-only arg 2' = 100,
            **kwargs: 'some extra keyword-only args') -> 'something':
    print(a, b, args, k1, k2, kwargs)
    