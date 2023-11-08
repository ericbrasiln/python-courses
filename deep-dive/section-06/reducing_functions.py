# video 92
# Reducing Functions

l = [5, 8, 6, 10, 9]

# reduce to a single value
_max = lambda x, y: x if x > y else y


def max_seq(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result


print(max_seq(l))

# reduce to a single value: min
_min = lambda a, b: a if a < b else b


def min_seq(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result


print(min_seq(l))


# reduce to a single value: sum
_sum = lambda a, b: a + b


def sum_seq(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _sum(result, x)
    return result


print(sum_seq(l))


def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


print("reduce function: max")
print(_reduce(_max, l))

print("reduce function: min")
print(_reduce(_min, l))

print("reduce function: sum")
print(_reduce(_sum, l))

# using reduce function from functools

from functools import reduce

print(reduce(_max, l))

print(reduce(_min, l))

print(reduce(_sum, l))

# reduce funcion work with any iterable object, including sets
print(reduce(_max, {5, 8, 6, 10, 9}))

# built-in functions for reduce
print(max(l))
print(min(l))
print(sum(l))
print(sum([1, 2, 3]))

# any and all

print(any([False, False, True]))
print(any([False, False, False]))

print(all([False, False, True]))
print(all([True, True, True]))

# factorial
# n! = 1 * 2 * 3 * ... * n
print(reduce(lambda a, b: a * b, range(1, 5+1)))
