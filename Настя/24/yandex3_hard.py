
f= open()
countA = 0
countO = 0
l = 0
r = -1
ans = 0
while r < len(f):
    while (countA <= 100 and countO <= 100):
        r += 1
        ans = max(ans, r - l + 1)
        if f[r] == 'A': countA += 1
        if f[r] == 'O': countO += 1
    while not(countA <= 100 and countO <= 100):
        if f[l] == 'A': countA -= 1
        if f[l] == 'O': countO -= 1
        l += 1