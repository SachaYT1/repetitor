

for n in range(100, 1000):
    nStr = str(n)
    a = sorted(nStr)
    maxNum = a[2] + a[1]


    if a[0] == '0' and a[1] == '0':
        minNum = a[2] + a[0]
    elif a[0] == '0':
        minNum = a[1] + a[0]
    else:
        minNum = a[0] + a[1]

    razn = int(maxNum) - int(minNum)
    if razn == 5:
        print(n)
        break


# '000'
# int('907')