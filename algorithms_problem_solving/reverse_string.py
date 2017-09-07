def reverse_string(s):
    l1 = list(s)
    l2 = []

    for i in range(len(l1)):
        l2.append(l1[-1])
        l1.pop()

    return "".join(l2)

s = 'hello'
print(reverse_string(s))
