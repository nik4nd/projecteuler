def gcd(a: int, b: int) -> int:
    while b > 0:
        a, b = b, a % b

    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


prev_lcm = 1
result = 0

for i in range(2, 21):
    prev_lcm = lcm(prev_lcm, i)
    if prev_lcm > result:
        result = prev_lcm

print(result)
