# Function Parameters

## Semantics

```
def my_func(a, b):
	# code
```

a and b are called *parameteres* of my_func, and they are *variables*, local to my_func.

When we call the function:

```
x = 10
y = 'a'

my_func(x, y)
```

x and y are called the *arguments* of my_func.

Also note that x and y are passed by reference (the memory addresses of x and y are passed.)

## Positional and keyword arguments

### Positional arguments

```
def my_func(a, b):
	# code

my_func(10, 20) # a = 10, b = 20

my_func(20,10) # a = 20, b = 10
```

#### Default values

Creates an optional parameter

```
def my_func(a, b=100):
	# code

my_func(10,20) #a = 10, b = 20

my_func(5) #a = 5, b = 100
```

What if we have three parameters, and we want to set the default value of the second parameter?

```
def my_func(a, b=100, c):
	# code
	# this is not allowed
```

If a positional parameter is defined with a default value every positional parameter after it must also be given a default value.

```
def my_func(a, b=5, c=10):
	# code
	# this is allowed

my_func(1) # a = 1, b = 5, c = 10

my_func(1, 2) # a = 1, b = 2, c = 10

my_func(1, 2, 3) # a = 1, b = 2, c = 3
```

How to specify values for a and c but let b take in its default value?

## Keyword arguments

(Also called named arguments)

```
def my_func(a, b=5, c=10):
	# code


my_func(a=1, c=2) # a = 1, b = 5, c = 2

my_func(1, c=2) # a = 1, b = 5, c = 2
```

Positional arguments can, optionally, be specified by using the parameter name whether or not the parameters have default values.


But once you use a named argument, all arguments thereafter must be named too.

## Code examples

```
def my_func(a, b, c):
	print(f'a={a}, b={b}, c={c}')
```

```
def my_func(a=1, b=2, c=3):
	print(f'a={a}, b={b}, c={c}')
```
