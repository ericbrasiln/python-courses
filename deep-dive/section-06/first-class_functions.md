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

## Lambda and Sorting

See [lambda_sorting.py](lambda_sorting.py)

## Challenge: randomly sort a list

See [challenge_sorted.py](challenge_sorted.py)

## Function introspection

Functions are first-class objects, so they have attributes.

We can attach our own attributes to functions.

```python
def my_func(a, b):
    return a + b

my_func.category = 'math'
my_func.sub_category = 'arithmetic'

print(my_func.category) # math
print(my_func.sub_category) # arithmetic
```

The `dir()` is a bulti-in function that returns the list of attributes of an object.

```python
dir(my_func)
```

### Function attributes

- `__doc__`: docstring
- `__annotations__`: annotations
- `__name__`: name of the function
- `__defaults__`: tuple containing positional parameter defaults
- `__kwdefaults__`: dictionary containing keyword-only parameter defaults
- `__code__`: code object representing the compiled function body, and thi object has many attributes
  - `co_varnames`: tuple containing parameter names and local variables => `my_func.__code__.co_varnames` => `('a', 'b')`
  - `co_argcount`: number of parameters (not including * and ** args) => `my_func.__code__.co_argcount` => `2`

### `inspect` module

```python
import inspect
```

What's the difference between a function and a method?

Classes and objects have attribtes - a n object that is bopund (to the class or the object).

An attribute that is calable, is called a method.

```python
def my_func(): # this function is not bound to anything. It is a function.
    pass

def_MyClass(): 
    def func(self): # this function is bound to an instance of the class. So it is a method and not a function.
        pass

my_object = MyClass()
```

Use inspect to know if an object is a function or a method:

```python
inspect.isfunction(my_func) # True
inspect.ismethod(my_func) # False
inspect.isfunction(func) # False
inspect.ismethod(func) # True

inspect.isfunction(my_object.func) # False
inspect.ismethod(my_object.func) # True

inspect.isroutine(my_func) # True
inspect.isroutine(func) # True
inspect.isroutine(my_object.func) # True
``` 

### Code introspection

We can recover the source code of our functions/methods.

```python
import inspect

inspect.getsource(my_func) # a string containing our entire def statement, including the docstring, annotations, etc.
```

We can find out in which module our function was created.


```python
inspect.getmodule(my_func) # <module '__main__'>

inspect.getmodule(print) # <module 'builtins' (built-in)>

inspect.getmodule(math.sin) # <module 'math' (built-in)>
```

### Function Comments

```python
# setting up a varible
i = 10

# TODO: Implement function
# some additional notes
def my_func(a, b=1):
    # comment inside my_func
    pass

inspect.getcomments(my_func) # '# TODO: Implement function\n# some additional notes\n'
```

### Callable signatures

```python
import inspect

inspect.signature(my_func)
```

Contains an attribute called parameters.

Esentially a dictionary of parameter names (keys) and mertadaa about the parameter (values).

- keys: parameter names
- values: objects with attributes such as name, default, annotatoin, kind.

`kind`:

- POSITIONAL_OR_KEYWORD
- VAR_POSITIONAL (for *args)
- KEYWORD_ONLY 
- VAR_KEYWORD (for **kwargs)
- POSITIONAL_ONLY (we cannot define it in python)

```python
import inspect

def my_func(:a 'a string',
            b: int = 1,
            *args: 'additional positional arguments',
            kw1: 'first keyword-only argument',
            kw2: 'second keyword-only argument' = 10,
            **kwargs: 'additional keyword-only arguments') -> str:
    """does something
       or other"""
    pass

for param in inspect.signature(my_func).parameters.values():
    print('Name:', param.name)
    print('Default:', param.default)
    print('Annotation:', param.annotation)
    print('Kind:', param.kind)
```

