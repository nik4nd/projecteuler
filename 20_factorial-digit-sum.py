num = 100
fact = 1
for i in range(num, 0, -1):
    fact *= i

fact = list(str(fact))
result = 0
for i in fact:
    result += int(i)

print(result)
