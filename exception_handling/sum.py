import collections

def sum(values):
    if not isinstance(values, collections.Iterable):
        raise TypeError('parameter must be an iterable type')
    total = 0
    for v in values:
        if not isinstance(v, (int, float,)):
            raise TypeError('elements must be numeric')
        total = total + v
    return total

lst = [1, 2, 3, 4, 5]
print(sum(lst))

# Raise an error.
print(sum(lst[0]))
