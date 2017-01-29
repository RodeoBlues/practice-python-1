def is_multiple(n, m):
    """ this function takes two integer values and
    returns True if n is multiple of m, that is, n = mi for
    some integer i, and False otherwise. """
    if n % m == 0:
        return True
    return False

print('50 is multiple of 10 is %s' % is_multiple(50, 10))
print('10 is multiple of 3 is %s' % is_multiple(10, 3))
print('6 is multiple of 3 is %s' % is_multiple(6, 3))
print('14 is multiple of 3 is %s' % is_multiple(14, 3))

def is_even(k):
    """ this function takes an integer value and returns True if k
    is even, and False otherwise. However, this function doesn't
    use multiplication, modulo, or division operators. """
    if k & 1 == 1:
        return False
    return True

print('3 is even number is %s' % is_even(3))
print('4 is even number is %s' % is_even(4))
print('5 is even number is %s' % is_even(5))
print('6 is even number is %s' % is_even(6))

def minmax(data):
    """ this function takes a sequence of one or more numbers, and
    returns the smallest and largest numbers, in the form of a tuple
    of length two. this function doesn't use the built-in functions
    min or max """
    try:
        smallest = data[0]
        largest = data[0]
        for n in range(1, len(data)):
            if data[n] < smallest:
                smallest = data[n]
            if data[n] > largest:
                largest = data[n]
        return smallest, largest
    except TypeError as e:
        print('Type error: {}'.format(e))

lst = [1, 2, 3, 4, 5, 6]
print(minmax(lst))

# an invalid parameter on purpose
print(minmax(12345))

lst = [-4, -3, -2, -1, 0, 1]
print(minmax(lst))

def square_sum_of_smallers(n):
    """ this function takes a positive integer n and returns the
    sum of the squares of all the positive integers smaller than n """
    if n <= 0 or not isinstance(n, (int,)):
        raise TypeError('The parameter should be a positive integer')
    sum_of_squares = 0
    i = 1
    while i < n:
        sum_of_squares += i * i
        i += 1
    return sum_of_squares

print('The square sum of smaller integers of {} is {}'.format(10, square_sum_of_smallers(10)))
print('The square sum of smaller integers of {} is {}'.format(5, square_sum_of_smallers(5)))
print('The square sum of smaller integers of {} is {}'.format(100, square_sum_of_smallers(100)))

def square_sum_comprehend(n):
    """ this function is another version of the function
    square_sum_of_smallers implemented using Python's comprehension
    syntax and the built-in sum function. """
    if n <= 0 or not isinstance(n, (int,)):
        raise TypeError('The parameter should be a positive integer.')
    total = sum(k*k for k in range(1, n))
    return total

print('The square sum of smaller integers of {} is {}'.format(10, square_sum_comprehend(10)))
print('The square sum of smaller integers of {} is {}'.format(5, square_sum_comprehend(5)))
print('The square sum of smaller integers of {} is {}'.format(100, square_sum_comprehend(100)))

# negative indices
lst = [1, 2, 3, 4, 5, 6]
print('at the index {} is {}'.format(1, lst[1]))
print('at the index {} is {}'.format(-5, lst[-5]))
print('at the index {} is {}'.format(-1, lst[-1]))
print('at the index {} is {}'.format(5, lst[5]))

def equiv_index(lst, i):
    """ Python allows negative integers to be used as indices into
    a sequence, such as a string. If string s has length n, and
    expression s[k] is used for index-n <= k < 0, what is the equivalent
    index j >= 0 such that s[j] references the same element?
    this function returns the equiv index of a parameter i """
    if i >= len(lst) or i < -len(lst):
        raise TypeError('The index should be in the range between {} and {}'
                .format(-len(lst), len(lst)-1))
    if i >= 0:
        return i - len(lst)
    return i + len(lst)

print('the equiv index of {} is {}'.format(-1, equiv_index(lst, -1)))
print('the equiv index of {} is {}'.format(-2, equiv_index(lst, -2)))
print('the equiv index of {} is {}'.format(2, equiv_index(lst, 2)))

# producing a range with values 50, 60, 70, 80
for n in range(50, 90, 10):
    print(n),

# producing a range with values 8, 6, 4, 2, 0, -2, -4, -6, -8
for n in range(8, -10, -2):
    print(n),

from random import randrange

def custom_choice(data):
    """ Python's random module includes a function choice(data)
    that returns a random element from a non-empty sequence.
    The random module includes a more basic function randrange,
    with parameterization similar to the built-in range function,
    that return a random choice from the given range.
    Using only the randrange function, this function implements
    the custom version of the built-in choice function. """
    try:
        i = randrange(0, len(data))
        return data[i]
    except TypeError as e:
        print('Type error: {}'.format(e))

data = "I'm a future Googler."
print('The chosen character of {} is {}'.format(data, custom_choice(data)))
print('The chosen character of {} is {}'.format(data, custom_choice(data)))
print('The chosen character of {} is {}'.format(data, custom_choice(data)))
print('The chosen character of {} is {}'.format(data, custom_choice(data)))
print('The chosen character of {} is {}'.format(data, custom_choice(data)))

def reverse(lst):
    """ This function reverses a list of n integers,
    so that the numbers are listed in the opposite order
    than they were before. """
    if not all(isinstance(n, int) for n in lst):
        raise TypeError('every element should be integer')

    for n in range(0, len(lst)//2):
        lst[n], lst[len(lst)-1-n] = lst[len(lst)-1-n], lst[n]

lst = [1, 2, 3, 4, 5]
reverse(lst)

print(lst)

def can_produce_odd(lst):
    """ This function takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence
    whose product is odd """
    if not all(isinstance(n, int) for n in lst):
        raise TypeError('every element should be integer')
    odds = 0
    for n in lst:
        if n & 1 == 1:
            odds += 1
            if odds >= 2:
                break
    return True if odds >= 2 else False

lst = [1, 2, 3, 4, 5]
print('a pair of numbers in {} can produce an odd is {}'.format(lst, can_produce_odd(lst)))
lst = [2, 3, 4, 6, 8]
print('a pair of numbers in {} can produce an odd is {}'.format(lst, can_produce_odd(lst)))

def are_distinct_numbers(lst):
    """ This function takes a sequence of integer values and determines
    if all the numbers are different from each other. """
    if not all(isinstance(n, int) for n in lst):
        raise TypeError('every element should be integer.')
    checker = 0
    for n in lst:
        if (1 << n) & checker > 0:
            return False
        checker |= 1 << n
    return True

lst = [1, 2, 3, 4, 5]
print('the list {} has all unique numbers is {}'.format(lst, are_distinct_numbers(lst)))
lst = [1, 2, 3, 4, 5, 1]
print('the list {} has all unique numbers is {}'.format(lst, are_distinct_numbers(lst)))

def is_unique_chars(s):
    """ This function checks if a string has all unique characters or not """
    if not isinstance(s, str):
        raise TypeError('the parameter should be a string')
    checker = 0
    for c in s:
        val = ord(c)
        if (1 << val) & checker > 0:
            return False
        checker |= 1 << val
    return True

s = 'test'
print('the string {} has all unique characters is {}'.format(s, is_unique_chars(s)))
s = 'abcd'
print('the string {} has all unique characters is {}'.format(s, is_unique_chars(s)))

# numeric types are immutable
lst = [1, 2, 3, 4, 5]
def scale(data, factor):
    """ this function is used to check whether numeric values in a list
    are mutable or not, numeric values are immutable. """
    for val in data:
        val *= factor

print(lst)
scale(lst, 2)
print(lst)

# produce a list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] using the comprehension syntax.
lst = [(i+1) * i for i in range(0, 10)]
print(lst)

# produce a list [ a , b , c ,..., z ] using the comprehension syntax.
print(ord('a'))
lst = [chr(i+ord('a')) for i in range(0, 26)]
print(lst)

from random import randint

def custom_shuffle(data):
    """ this function works like the built-in function shuffle
    using only the basic function randint(a, b). """
    try:
        for i in range(0, len(data)):
            r = randint(0, len(data)-1)
            data[i], data[r] = data[r], data[i]
    except TypeError as e:
        print('Type error:{}'.format(e))

lst = [1, 2, 3, 4, 5]
custom_shuffle(lst)
print(lst)

import sys

def read_lines():
    try:
        lines = list()
        for line in sys.stdin:
            lines.append(line.replace('\n', ''))
        for i in range(len(lines)-1, -1, -1):
            print(lines[i])
    except EOFError as e:
        print('EOF error: {}'.format(e))

def dot_products(a, b):
    if len(a) != len(b):
        raise TypeError('the length of two lists should be same')
    if len(a) == 0 or len(b) == 0:
        raise TypeError('the length of any list cannot be 0')
    if not all(isinstance(n, int) for n in a) or not all(isinstance(n, int) for n in b):
        raise TypeError('every element in each list should be integer')
    return [a[n] * b[n] for n in range(0, len(a))]

lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
print(lst1)
print(lst2)
print(dot_products(lst1, lst2))

# index out of bounds
lst = [1, 2, 3, 4, 5]
try:
    lst[5] = 6
except IndexError as e:
    print("Don't try buffer overflow attacks in Python!")

def sorted_factors(n):
    """ this function yield the factors in increasing order. """
    k = 1
    lst = list()
    while k * k < n:
        if n % k == 0:
            yield k
            lst.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for i in sorted(lst):
        yield i

for n in sorted_factors(100):
    print(n),

def norm(v, p=None):
    p = p or len(v)
    return sqrt((sum([x**p for x in v])))

def words(letters, word=''):
    """ this program outputs all possible strings
    formed by using given characters exactly once. """
    letters or print(word)
    for letter in letters:
        words(letters - {letter}, word + letter)

words(set('catdog'))

def division_times_by_two(n):
    if n <= 2:
        raise TypeError('the parameter should be greater than 2')
    count = 0
    while n > 2:
        n /= 2
        count += 1
    return count

print(division_times_by_two(100))
print(division_times_by_two(1024))

def make_change(charged, given):
    """ this function takes two numbers as input,
    one that is a monetary amount charged and the other
    that is a monetary amount given. It should then return
    the number of each kind of bill and coin to give back
    as change for the difference between the amount given
    and the amount charged. """
    if charged > given:
        raise TypeError('The amount given should be greater than the amount charged')
    change = {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0, 'C': 0}
    deducted = given - charged
    change['C'] = int(str(round(deducted - int(deducted), 2))[2:])
    deducted = int(deducted)
    while deducted > 0:
        if deducted >= 100:
            change['100'] = deducted // 100
            deducted = deducted % 100
        elif deducted >= 50:
            change['50'] = deducted // 50
            deducted = deducted % 50
        elif deducted >= 20:
            change['20'] = deducted // 20
            deducted = deducted % 20
        elif deducted >= 10:
            change['10'] = deducted // 10
            deducted = deducted % 10
        elif deducted >= 5:
            change['5'] = deducted // 5
            deducted = deducted % 5
        elif deducted >= 2:
            change['2'] = deducted // 2
            deducted = deducted % 2
        else:
            change['1'] = deducted
            deducted -= 1
    return change

print(make_change(59.49, 100))
