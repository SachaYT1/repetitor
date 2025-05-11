f = open('KEGE 26 20910.txt')

n, m, k = map(int, f.readline().split())


seats = {}

for i in range(1, k + 1):
    seats[i] = m + 1

for i in range(n):
    row, seat = map(int, f.readline().split())
    if row < seats[seat]:
        seats[seat] = row


maxRow = 0
minSeat = 10 ** 9
for i in range(1, k):
    if min(seats[i], seats[i + 1]) - 1 > maxRow:
        maxRow = min(seats[i], seats[i + 1]) - 1
        minSeat = i

print(maxRow, minSeat)

