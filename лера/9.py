summa = 0
n = 0
num = int(input())
while (num != 0):
    if 9 < num < 100:
        n += 1
        summa += num
    num = int(input())

if n != 0:
    arifm = summa / n
    print(round(arifm, 1))
else:
    print('NO')