a, b = 1, 2
a = b
b = a
print(a, b, sep=', ')

t = a
a = b
b = t
print(a, b, sep=', ')