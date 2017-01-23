# automatic packing
data = 2, 4, 6, 8
print(data)

# unpacking a sequence
a, b, c, d = range(7, 11)
print("{}, {}, {}, {}".format(a, b, c, d))

quotient, remainder = divmod(a, b)
print("{}, {}".format(quotient, remainder))

for x, y in [(7, 2), (5, 8), (6, 4),]:
    print("{}, {}".format(x, y))

d = dict()
d['a'] = 'a'
d['b'] = 'b'
d['c'] = 'c'

for k, v in d.items():
    print("{}, {}".format(k, v))

# simultaneous assignments
x, y, z = 6, 2, 5
print("{}, {}, {}".format(x, y, z))

def fibonacci(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a+b
        i = i + 1

for n in fibonacci(10):
    print(n),
