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

## Identifier names

>video 7
