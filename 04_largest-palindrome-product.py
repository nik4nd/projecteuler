result = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        num = i * j
        numList = list(str(num))

        while len(numList) > 1:
            if numList[0] == numList[-1]:
                numList.remove(numList[0])
                numList.remove(numList[-1])
                if len(numList) == 0 or len(numList) == 1:
                    if num > result:
                        result = num
            else:
                break

print(result)
