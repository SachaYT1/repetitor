f = open('KEGE 18030.txt')

n = int(f.readline())


cards = []
for i in range(n):
    cards.append(int(f.readline()))

cards.sort()

countLevel = 0
minSum = 0

flag = True
i = 1
countCards = 0 
while (flag): 
    if (n - countCards >= i):
        pass
    else:
        break

    countCards += i
    i = i + 1
    countLevel += 1

minSum = sum(cards[0:countCards])
print(countLevel, minSum)
"""
140 491509192

140 491607804"""

