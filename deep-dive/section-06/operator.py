# video 96

import operator
from functools import reduce
from operator import is_

print(dir(operator))

print(operator.add(1, 2))

print(operator.mul(3, 2))

print(operator.truediv(3, 2))

print(operator.floordiv(13, 2))

r = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(r)

r = reduce(operator.mul, [1, 2, 3, 4])
print(r)

print(operator.lt(10, 3))

print(is_('abc', 'def'))

print(operator.is_('abc', 'def'))

print(operator.truth([]))

print(operator.truth([1]))

my_list = [1, 2, 3, 4]

print(my_list[1])

print(operator.getitem(my_list, 1))

print(operator.setitem(my_list, 1, 100))

my_list = [1, 2, 3, 4]

operator.setitem(my_list, 1, 100)

print(my_list)

operator.delitem(my_list, 3)
print(my_list)

f = operator.itemgetter(2)

print(f(my_list))

s = 'python'

print(f(s))

f = operator.itemgetter(2, 3)

print(f(my_list))

# attrgetter

class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')

obj = MyClass()

print(obj.a)
print(obj.b)
print(obj.c)
print(obj.test)
print(obj.test())

prop_a = operator.attrgetter('a')
print(prop_a(obj))
