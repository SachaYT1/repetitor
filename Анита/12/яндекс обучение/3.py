ans = []
for n in range(203 + 1):
    s = (203 - n) * '1' + '2' + n * '1'
    while '111' in s or '222' in s:
        if '111' in s:
            s = s.replace('111', '22', 1)
        else:
            s = s.replace('222', '11', 1)

    ans.append(s)

ans.sort(key=len, reverse=True)
print(ans)