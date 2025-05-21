summa = 0
num = int(input())
while (num != 0):
    if num % 8 == 0 and num % 10 == 6:
        summa = summa + num
    num = int(input())
print(summa)

