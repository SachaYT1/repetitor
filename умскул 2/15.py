countA = 0
for a in range(1, 1000):
    fl = True
    for x in range(100):
        for y in range(100):
            f = (not(x > 18) or (x * y + 14 * x >= a)) and (not(y * x + y > a) or (y >= 3))
            if not f:
                fl = False
                break
        if not fl:
            break
    if fl:
        countA += 1
print(countA)