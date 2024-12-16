f = open('demo_2025_26.txt')

n = int(f.readline())
n_stip = int(0.25 * n)
students = []
a = []
b = []
for i in range(n):
    s = f.readline().split()
    id, x, y, z, w = int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4])
    if x != 2 and y != 2 and z != 2 and w != 2:
        a.append([id, (x + z + w + y) / 4])
    if s[1:].count('2') > 2:
        b.append([int(s[0]), int(s[1:].count('2'))])
# сортируем список сначала по убыванию среднего балла, а затем по возрастанию id
a.sort(key=lambda k: (-k[1], k[0]))
b.sort(key=lambda k: (k[1], k[0]))
print(a)
print(b)
# id, ответ на первую часть
print(a[n_stip - 1][0])
# id, ответ на вторую часть
print(b[0][0])
