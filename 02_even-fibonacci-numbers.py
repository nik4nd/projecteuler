second_prev = 1
first_prev = result = 2
next_num = 0

while next_num < 4000000:
    next_num = first_prev + second_prev
    if next_num % 2 == 0:
        result += next_num
    second_prev, first_prev = first_prev, next_num

print(result)
