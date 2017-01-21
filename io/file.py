import sys
import os

with open('test.txt', 'a+') as fp:
    print(fp.read(10))
    print('The current position is {}'.format(fp.tell()))
    print(fp.read())

    fp.seek(0)
    print(fp.readline())
    print('The current position is {}'.format(fp.tell()))
    print(fp.readlines())
    print('The current position is {}'.format(fp.tell()))

    fp.seek(0)
    for line in fp:
        print(line)
        print('The current position is {}'.format(fp.tell()))

    fp.seek(os.stat('test.txt').st_size)
    fp.write("That's why I'm learning Python very hard even in weekend.\n")
    fp.seek(0)
    sys.stdout = open('another_test.txt', 'w')
    print('{}'.format(fp.read()))
