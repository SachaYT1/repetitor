f = open('KEGE 26 20910.txt')

n, m, k = map(int, f.readline().split())

zal = {}

for i in range(1, k + 1):
    zal[i] = m + 1

for i in range(n):
    row, seat = map(int, f.readline().split())
    if zal[seat] > row:
        zal[seat] = row

maxRow = 0
minSeat = 10**9
for i in range(1, k):
    if min(zal[i], zal[i + 1]) - 1 > maxRow:
        maxRow = min(zal[i], zal[i + 1]) - 1
        minSeat = i

print(maxRow, minSeat)
