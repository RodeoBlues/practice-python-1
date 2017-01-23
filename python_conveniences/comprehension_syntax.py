n = 10
squares = []
for k in range(1, n+1):
    squares.append(k*k)
print(squares)

squares = [k*k for k in range(1, n+1)]
print(squares)

factors = [k for k in range(1, n+1) if n % k == 0]
print(factors)

# The generator syntax is particularly attractive when results do not need to be stored in memory.
total = sum(k*k for k in range(1, n+1))
print(total)
