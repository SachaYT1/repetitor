f = open('24-215.txt').readline()

m = 0
for j in 0, 1, 2: # индекс с какого начинаем проверять тройки
    c = 0
    for i in range(j, len(f) - 2, 3):
        if f[i] in 'ABC' and f[i + 1] in '123' and f[i + 2] in '123':
            c += 1
            m = max(m, c)
        else:
            c = 0
print(m)