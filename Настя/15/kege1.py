ans = []
for a in range(1, 3000):
    flag = True
    for x in range(1, 3000):
        f = not((x % a == 0) and (x % 24 == 0) and not(x % 16 == 0)) or not(x % a == 0)
        if not f:
            flag = False
            break
    if flag:
        ans.append(a)
print(min(ans))