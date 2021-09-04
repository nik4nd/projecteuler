num = temp = 600851475143
divider = 2

while divider < num**0.5 and temp != 1:
    if temp % divider == 0:
        temp /= divider
    else:
        divider += 1

print(divider)
