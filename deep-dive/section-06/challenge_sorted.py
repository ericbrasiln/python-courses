import random
random.random()

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# to randomly order the list we use a lambda function.
sorted(l, key=lambda s: s.random.random())

#this same lambda function can be translated to def function:
# def random_sort(s):
    # return s.random.random()