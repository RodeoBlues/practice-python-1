print('abs(-2) returns {0}'.format(abs(-2)))
lst = [1, 1, 1, 2, 3]
print('all({0}) returns {1}'.format(str(lst), all(lst)))
print('any({0}) returns {1}'.format(str(lst), any(lst)))
lst = [0, 1, 0, 0, 0]
print('all({0}) returns {1}'.format(str(lst), all(lst)))
print('any({0}) returns {1}'.format(str(lst), any(lst)))
i = 65
print('chr({0}) returns {1}'.format(i, chr(i)));
x = 12
y = 5
print('divmod({0}, {1}) returns {2}'.format(x, y, str(divmod(x, y))))
obj = 'test'
print('hash({0}) returns {1}'.format(obj, hash(obj)))
print('id({0}) returns {1}'.format(obj, id(obj)))
print('isinstance({0}, {1}) returns {2}'.format(obj, str, isinstance(obj, str)))
print('iter({0}) returns {1}'.format(lst, str(iter(lst))))
print('len({0}) returns {1}'.format(lst, len(lst)))
def sqrt(x): return x ** 2
print('map({0}, {1}) returns {2}'.format(str(sqrt), lst, map(sqrt, lst)))
print('max({0}) returns {1}'.format(str(lst), max(lst)))
print('max({0}, {1}, {2}) returns {3}'.format(i, x, y, max(i, x, y)))
print('min({0}) return {1}'.format(str(lst), min(lst)))
print('min({0}, {1}, {2}) returns {3}'.format(i, x, y, min(i, x, y)))
it = iter(lst)
print('next({0}) returns {1}'.format(str(it), next(it)))
print('next({0}) returns {1}'.format(str(it), next(it)))
print('next({0}) returns {1}'.format(str(it), next(it)))
print('next({0}) returns {1}'.format(str(it), next(it)))
c = 'A'
print('ord({0}) returns {1}'.format(c, ord(c)))
print('pow({}, {}) returns {}'.format(x, y, pow(x, y)))
print('pow({}, {}, {}) returns {}'.format(x, y, y, pow(x, y, y)))
print('print({}, {}, {}) returns'.format(i, x, y))
print(i, x, y)
print('range({}) returns {}'.format(x, range(12)))
print('range({}, {}) returns {}'.format(y, x, range(y, x)))
print('range({}, {}, {}) returns {}'.format(y, x, y, range(y, x, y)))
it = reversed(lst)
print('reversed({}) returns {}'.format(str(lst), next(it)))
print('reversed({}) returns {}'.format(str(lst), next(it)))
print('reversed({}) returns {}'.format(str(lst), next(it)))
print('reversed({}) returns {}'.format(str(lst), next(it)))
print('reversed({}) returns {}'.format(str(lst), next(it)))
f = 3.1412
print('round({}) returns {}'.format(f, round(f)))
k = 2
print('round({}, {}) returns {}'.format(f, k, round(f, k)))
print('sorted({}) returns {}'.format(lst, str(sorted(lst))))
it = iter(lst)
print('sum({}) returns {}'.format(str(it), sum(it)))
print('type({}) returns {}'.format(lst, type(lst)))
print('type({}) returns {}'.format(c, type(c)))
print('type({}) returns {}'.format(k, type(k)))
print('type({}) returns {}'.format(str(it), type(it)))
