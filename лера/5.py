summa = 0
num = int(input())
while (num != 0):
    if num % 4 == 0 and num % 10 == 8:
        summa += num
    num = int(input())
print(summa)