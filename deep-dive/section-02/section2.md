# Quick Refresher

## Python Hierarchy 

>video 5

### Numbers

- Integral: integers, booleans
- Non-integral: floats; complex; Decimals; fractions

### Collections

- Sequences
  - Mutable: lists
  - Immutable: tuples, strings
- Sets
  - mutable: sets
  - immutable: frozen sets
- Mappings
  - Dictionaries
  
### Callable

- user-defined functions
- generators
- classes
- instance methods
- class instances (`__call__()`)
- built-in functions (e.g. `len()`)
- built-in methods (e.g. `list.append(x)`)

### Singletons

- None
- NotImplemented
- Ellipsis(...)

## Multi-line Statements and strings

>video 6

Human Readability is important.

### Implicit line joining

Expressions in:

- lists literals: []
- tuple literals: ()
- dictionary literals: {}
- set literals: {}
- function arguments / parameters
  - supports inline comments

```python
def my_fun(a,
           b, #comment
           c):
    print(a, b, c)

my_fun(10, #comment 
       20, 30)
```

### Explicit line joining

- backslash `\`

That's not gonna work:

```python
if a
    and b \
    and c:
    print('yes')
```

This is the correct way:

```python
if a \
    and b \
    and c:
```

:warning: Comments cannot be part of a statement, not even a multi-line statement.

### Multi-line strings literals

- triple quotes `'''` or `"""`

:warning: These are not comments.

```python

```

## Variable names

>video 7

- case-sensitive
- **must** start with a letter or underscore
- followed by letters, numbers, or underscores
- cannot be a reserved word

### Conventions

- beginning with an underscore `_` for internal use
- double underscore `__` for name mangling 
- beginning and ending with double underscores `__` for special methods
- package names: all lowercase, no underscores
- modules: all lowercase, can have underscores
- Classes: CapWords (upper camel case)
- Functions: snake_case
- Variables: snake_case
- Constants: ALL_CAPS separated by underscores
  
## Conditionals

>video 8

### if / elif / else

### Ternary operator

```python
x = 10 if a > 10 else 20
```

## Functions

>video 9

- built-in functions: e.g. `len()`
- To create a function, use the `def` keyword; followed by the function name, parentheses, and a colon

```python
def func_1():
  a + b
```

- functions inside functions

```python
def func_2():
  return func_3()

def func_3():
  print('hello')
```

### lambda functions

- anonymous functions

```python
lambda x: x + 1
```

## While loop

>video 10

```python
i = 5
while i < 5:
  print(i)
  i += 1
```

### break

Terminates the loop imidiatly

```python
 i = 5
while True:
    print(i)
    if i >=5:
      break
      print('something')
```

e.g.

```python
min_length = 2
name = input("Please enter your name: ")

while not(len(name) >= min_lenght and name.isprintable() and name.isalpha()):
  name = input("Please enter your name: ")

print(f"Hello {name}")
```

or:

```python
min_length = 2
while True:
  name = input("Please enter your name: ")
  if len(name) >= min_lenght and name.isprintable() and name.isalpha():
    break
print(f"Hello {name}")
```

### Continue statement

- skips the rest of the current iteration

```python
a = 0 

while a < 10:
  a += 1
  if a % 2 == 0:
    continue
  print(a)
```

## else clause in while loop

```python
l = [1,2,3]
val = 10

found = False
idx = 0

while idx < len(l):
  if l[idx] == val:
    found = True
    break
  idx += 1

ifnot found:
  l.append(val)

print(l)
```

Now with `else`:

```python
l = [1,2,3]
va = 10
idx = 0
while idx < len(l):
  if l[idx] == val:
    break
  idx += 1
else:
  l.append(val)
print(l)
```

## Break, continues and try statements

>video 11

- try, except, finally
- finally is always executed

```python
a = 10
b = 1
try:
  a/b
except ZeroDivisionError:
  print('division by zero')
finally:
  print('always executed')
```


