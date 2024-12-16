from itertools import product
a = product('ГИПЕРБОЛА', repeat=6)
count = 0
count1 = 0
for i in a:
    s = ''.join(i)
    glas = ['И', 'Е', 'О', 'А']
    soglas = ['Г', 'П', 'Р', 'Б', 'Л']

    if s[0] not in glas and s[-1] not in glas:
        count += 1
        flag = True
        for j in range(1, len(s) - 1):
            if s[j] in glas:
                if s[j - 1] in soglas and s[j + 1] in soglas:
                    count -= 1
                    flag = False
                    break
        if flag:
            count1 += 1

print(count1)
