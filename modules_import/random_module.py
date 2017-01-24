from random import *

seed('test')
print(random())
print(randint(0, 10))
print(randrange(0, 10, 2))
print(choice('test2'))
lst = [0, 1, 2, 3, 4, 5]
shuffle(lst)
print(lst)

