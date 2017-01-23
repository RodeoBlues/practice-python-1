def factors(n):
    for k in range(1, n+1):
        if n % k == 0:
            yield k

for factor in factors(60):
    print(factor),

print("")

for factor in factors(12):
    print(factor),
