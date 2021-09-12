sieve = list(range(104750))
sieve[1] = 0
for i in sieve:
    if i > 1:
        for j in range(2*i, len(sieve), i):
            sieve[j] = 0
sieve = list(set(sieve))
sieve.remove(0)

print(sorted(sieve)[-1])
