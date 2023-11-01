# First-class functions

- can be passed toa function as an argument
- can be returned from a function
- can be assigned to a variable
- can be stored in a data structure (such as list, tuple, dictionary, etc.)

Type such as int, float, string, tuple, list and many others are first-class objects in Python.

Functions (function) are also first-class objects in Python.

## Higher-Order functions

- take a function as an argument
- return a function as the return value

## Topics in this section

1. function annotation and documentation
2. lambda expressions and anonymous functions
3. callables
4. function introspection
5. built-in higher-order functions (such as sorted, map, filter)
6. some functions in the functools module (such as redduce, all, any)
7. partials

## 1. function annotation and documentation

### Docstrings

Is defined at PEP 257.

If the first line of a functions is a string, it will be interpreted as a docstring.

```python
def func(a):
    "documentation for func"
    return a
```

Multi-line are also supported:

```python
def func(a):
    """
    documentation for func
    more details
    """
    return a
```

Where they are stored?

Docstringsd are stored in the `__doc__` attribute of the function.

```python
def func(a):
    """
    documentation for func
    more details
    """
    return a

print(func.__doc__)
```

Is used toa attache metadata to functions.

### Function annotations

Is defined at PEP 3107.

```python
def my_func(a: <expression>, b: <expression>) -> <expression>:
    pass
```

Here is a practical example:

```python
def my_func(a: 'a string', b: 'a positive integer') -> 'a string':
    return a * b

help(my_func)
```

In this case, my_func.__doc__ will be empty. 

This is only metadata, it does not enforce anything.

- Annotations can be any expression:

```python
def my_func(a: str, b: 'int > 0') -> str:
    return a * b
```

- Annotations are stored in the `__annotations__` attribute of the function. And it is a dictionary. Keys are the parameter names. The values ar the annotations.

Where Python use docstrings and annotations? It doesn't use. Mainly used by external tools and modules.

## 2. lambda expressions

lambda is another way to create functions. Also called anonymous functions.

![](lambda.png)

### Examples

```python
lambda x: x ** 2

lambda x, y: x + y

lambda : 'hello'

lambda s: s[::-1].upper()
```

All this objects as function objects, but not "named".

lambdas are not equivalent to closures.

```my_func = lambda x: x ** 2``` is the same as ```def my_func(x): return x ** 2```

### Limitations

- the "body" of a lambda is limited to a single expression
- no assignments
- no annotations
- single line of code

