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

## Unpacking iterables

Pack values: tuples, sets, dictionaries

Unpacking is the act os spliting packed values into individuals variables contained in a list or tuple.

```
a, b, c = [1, 2, 3]
```

The unpacking into individual variables is based ion the relative positions of each element.

Like the positional arguments in function.

- unpacking tuples = `a,b,c = 10, 20, 'hello'`
- unpacking strings = `a,b,c = 'XYZ'`

Unpacking works in any iterable type.

### Swapping values of two variables

a = 10
b = 20

Using unpacking = `a, b = b,  a`

The left side is evaluated first and python creates a tuple in memory, and then the assingments are made in the right side.

### Unpacking sets and  dictionaries

d = {'key1':1, 'key2':2, 'key3':3}

for e in d  => e iterates through the keys. So we unpack only the keys of d.

Dicts and Sets are unordered types, and so there is no guarantee the order of the results. In practice is rare to unpack sets and dictionaries in this way.

## Extended unpacking

```
l = [1,2,3,4,5,6]

a, b = l[0], l[:1] #or a, b = l[0], l[:1]
```

Or we can use the `*` operator: `a, *b = l` 

- usage with ordered types:

a, b* = [-10, 5, 2, 100] => a = -10 b = [5, 2, 100]
a, b* = (-10, 5, 2, 100) => a = -10 b = [5, 2, 100]
a, b, *c = 1, 2, 3, 4, 5 => a= 1 b = 2 c = [3, 4, 5]
a, b, *c, d = 1, 2, 3, 4, 5 => a= 1 b = 2 c = [3, 4] d = 5

it works with strings as well

The * operator can be used only one time in the left-hand side.

- unordered types

AS we cannot count on the order, we rearely unpack sets and fictionaries in this way.

But it is used in the right-hand side.

d1 = {'p':1, 'y':2}
d2 = {'t':3. 'h':4}
d3 = {'h':7, 'o':5, 'n': 6}

l = [*d1, *d2, *d3] => ['p','y','t','h','h','o','n']
s = {*d1, *d2, *d3} => {'p','y','t','h','o','n'}

**The order is not guaranteed**


- Using `**` operator


d1 = {'p':1, 'y':2}
d2 = {'t':3. 'h':4}
d3 = {'h':7, 'o':5, 'n': 6}

d = {**d1, **d2, **d3} => {'p',:1 'y':2 ,'t':3 ,'h':7,'o':5,'n':6}

- Nested unpacking

l = [1, 2, [3, 4]]

a, b, (c, d) = l  => a = 1 b = 2 c = 3 d = 4

- 2 `*` operators in left-hand side?

a, *b, (c, *d) = [1, 2, 3, 'python']

a = 1
b = [2, 3]
c = 'p'
d = ['y', 't', 'h', 'o', 'n']

## *args

```
def func1(a, b, *c):
    # code
```

func1(10, 20, 'a', 'b') => a = 10 b = 20 c = ('a', 'b') :warning: This is a tuple, not a list

Convenctio = call it `*args`

```
def func1(a, b, *args):
    # code
```

*args exhausts positional arguments: you cannor add more positional arguments after *args

- Unpacking arguments

def func2(a, b, c):
    #code

l = [10, 20, 30]

this will not work: func2(l)

But we can unpack the list first and then pass it to the function:

func2(*l) => a = 10 b = 20 c = 30
