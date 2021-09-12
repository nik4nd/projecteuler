for n in range(1, 6):
    for m in range(n+1, 21):
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if a+b+c == 1000:
            print(a*b*c)
