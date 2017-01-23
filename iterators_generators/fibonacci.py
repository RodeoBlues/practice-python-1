def fibonacci(n):
    a = 0
    b = 1
    while a <= n:
        yield a
        future = a + b
        a = b
        b = future

for n in fibonacci(10):
    print(n),
