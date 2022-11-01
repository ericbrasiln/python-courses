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