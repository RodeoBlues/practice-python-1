def reverse(lst):
    ''' This function reverses a list of n integers,
    so that the numbers are listed in the opposite order
    than they were before. '''
    if not all(isinstance(n, int) for n in lst):
        raise TypeError('every element should be integer')

    for n in range(0, len(lst)/2):
        lst[n], lst[len(lst)-1-n] = lst[len(lst)-1-n], lst[n]

lst = [1, 2, 3, 4, 5]
reverse(lst)

print(lst)

def can_produce_odd(lst):
    ''' This function takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence
    whose product is odd '''
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
    ''' This function takes a sequence of integer values and determines
    if all the numbers are different from each other. '''
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
    ''' This function checks if a string has all unique characters or not '''
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
