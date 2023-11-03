l = ['c', 'B', 'D', 'a']
print(l)

sorted(l, key=lambda s: s.upper())


d = {'def': 300, 'abc': 200, 'ghi': 100}

sorted(d)

# sort by value
sorted(d, key=lambda e: d[e])

def dist_sq(x):
    """Returns the distance of a point from the origin
    .real and .imag are the attributes of complex numbers"""
    return (x.real)**2 + (x.imag)**2

l = [3+3j, 1-1j, 0, 3+0j]

# sort by distance from origin
sorted(l, key=dist_sq)

# using lambda
sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2)

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']

sorted(l)

# sorte by the last character
sorted(l, key=lambda s: s[-1])

# Python use stable sorting so the order of the elements with the same key is preserved