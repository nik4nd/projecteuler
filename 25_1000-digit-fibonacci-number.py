second_prev = 1
first_prev = 2
next_num = 0
i = 3

while len(str(next_num)) != 1000:
    next_num = first_prev + second_prev
    i += 1
    second_prev, first_prev = first_prev, next_num

print(i)
