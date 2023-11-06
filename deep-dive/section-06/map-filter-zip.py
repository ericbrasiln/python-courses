# video 90
# map function

def fact(n):
    return 1 if n == 0 else n * fact(n-1)


fact(3)


results = list(map(fact, range(6)))

print(results)

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
l3 = 100, 200, 300, 400

results = list(map(lambda x, y, z: x+y+z, l1, l2, l3))

print(results)

# filter function
list(filter(lambda x: x % 3 == 0, range(25)))

list(filter(None, [1, 0, 4, 'a', '', None, True, False]))

# zip function
l1 = [1, 2, 3, 4]
l2 = [10, 20, 30]
l3 = 'python'

results = list(zip(l1, l2, l3))

for x in results:
    print(x)

list(zip(range(10000), 'python'))

l = range(10)

print(list(l))

list(map(fact,l))

results = [fact(n) for n in range(10)] # list

results = (fact(n) for n in range(10)) # generator

for x in results:
    print(x) # generator is iterable only once

# to make generator iterable multiple times
# use list comprehension
results = [fact(n) for n in range(10)] # list

l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40]

list(map(lambda x, y: x + y, l1, l2))

[x + y for x, y in zip(l1, l2)] # same as above using list comprehension

list(filter(lambda x: x % 2 == 0, map(lambda x, y: x + y, l1, l2)))

[x + y for x, y in zip(l1, l2) if (x + y) % 2 == 0] # same as above using list comprehension


