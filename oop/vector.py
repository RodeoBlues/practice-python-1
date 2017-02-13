class Vector:
    """ Represent a vector in a multidimensional space. """

    def __init__(self, d):
        """ Create d-dimensional vector of zeros, or
        create a vector with a list.
        """
        if isinstance(d, int):
            self._coords = [0] * d
        elif isinstance(d, list):
            self._coords = d

    def __len__(self):
        """ Return the dimension of the vector. """
        return len(self._coords)

    def __getitem__(self, j):
        """ Return jth coordinate of vector. """
        return self._coords[j]

    def __setitem__(self, j, val):
        """ Set jth coodinate of vector to given value. """
        self._coords[j] = val

    def __add__(self, other):
        """ Return sum of two vectors. """
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __mul__(self, other):
        """ Returns a new vector with coordinates that are n times. """
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * other[j]
        return result

    def __rmul__(self, n):
        """ Returns a new vector with coordinates that are n times. """
        return self.__mul__(n)

    def __radd__(self, other):
        """ Return sum of two vectors. """
        return self.__add__(other)

    def __sub__(self, other):
        """ Return difference between two vectors. """
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self._coords[j] * -1
        return result

    def __eq__(self, other):
        """ Return True if vector has same coordinates as other. """
        return self._coords == other._coords

    def __ne__(self, other):
        """ Return True if vector differs from other. """
        return not self == other

    def __str__(self):
        """ Produce string representation of vector. """
        return '<' + str(self._coords)[1:-1] + '>'


v = Vector(5)
v[1] = 23
v[-1] = 45
print(v[4])
u = v + v
print(u)
total = 0
for entry in v:
    total += entry
print(total)
print(str(v))

v2 = Vector(5)
v2[1] = 23
v2[-1] = 45

print('Multiplication of {} and {} is {}'.format(v, v2, v * v2))
u = v + [5, 3, 10, -2, 1]
print('u is {}'.format(u))
u = [5, 3, 10, -2, 1] + v
print('u is {}'.format(u))

print(v is v2)
print(v == v2)
print('the difference between two vectors {}, {} is {}'.format(v, v2, v - v2))
import copy
copy_of_v = copy.deepcopy(v)
print('negated values of vector {} is {}'.format(copy_of_v, -v))

v3 = Vector([1, 2, 3, 4, 5])
print('the newly created vector is {}'.format(v3))
