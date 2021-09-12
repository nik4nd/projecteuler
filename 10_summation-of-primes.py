sieve = list(range(2000001))
sieve[1] = 0
for i in sieve:
    if i > 1:
        for j in range(2*i, len(sieve), i):
            sieve[j] = 0
sieve = list(set(sieve))
sieve.remove(0)

result = 0
for i in sieve:
    result += i

print(result)
