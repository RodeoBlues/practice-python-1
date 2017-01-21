def sqrt(x):
    if not isinstance(x, (int, float,)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')
    return x ** 0.5

print(sqrt(100))
print(sqrt(4))
print(sqrt(9))

# Raise an error
print(sqrt(-7))
