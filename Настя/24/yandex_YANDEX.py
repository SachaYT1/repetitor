
f = 'DFFSDENDNDDNEFEDSFWE'
f = f.split('E')
print(f)

c_max = 0
for i in range(1, len(f) - 1):
    string = f[i]
    flag = True
    for letter in string:
        if not(letter == 'D' or letter == 'N'):
            flag = False
            break
    if flag:
        c_max = max(c_max, len(string) + 2)

    print(c_max)