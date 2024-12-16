
f = open('24-s1.txt', 'r').readlines()
count = 0
for s in f:
    flag = False
    for j in range(len(s) - 2):
        if s[j] == 'F' and s[j + 2] == 'O':
            flag = True
            break
    if flag:
        count += 1
print(count)