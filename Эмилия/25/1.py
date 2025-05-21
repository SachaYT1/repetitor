a = set()
from math import ceil, floor

a.add(2)

a.add(3)

a.add(4)

a.add(2)






def deliteli(num):
    a = set()
    for i in range(1, round(num ** 0.5) + 1):
        if num % i == 0:
            a.add(i)
            a.add(num // i)
    return a


{1, 2, 5, 7, 3}
for x in range(154_026, 154_043 + 1):
    delX = deliteli(x)
    if len(delX) == 4:
        listDelX = list(delX)
        listDelX.sort()
        print(listDelX[-2], listDelX[-1])



