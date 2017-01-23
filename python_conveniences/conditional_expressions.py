def foo(p):
    return p

n = 1
if n >= 0:
    param = n
else:
    param = -n

result = foo(param)
print(result)

n = -2

param = n if n >= 0 else -n
result = foo(param)
print(result)

result = foo(n if n >= 0 else -n)
print(result)
