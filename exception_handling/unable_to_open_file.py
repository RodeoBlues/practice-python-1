try:
    fp = open('unknown.txt')
except IOError as e:
    print('Unable to open the file:', e)
