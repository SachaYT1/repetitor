ans = []
for n in range(108, 5000, 9):
    s = n * '5'

    while '555' in s or '11' in s or '2' in s:
        s = s.replace('555', '1', 1)
        s = s.replace('11', '25', 1)
        s = s.replace('2', '5', 1)

    ans.append([int(s), n])

ans.sort(key=lambda x: (-x[0], x[1]))
print(ans)
print(ans[0][1])
