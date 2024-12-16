count = 0
for a in range(1, 1000):
    flag = True
    for x in range(0, 1000):
        for y in range(1000):
            if not((not(x > 8) or (x * y + 2 * x >= a)) and (not(y * y + y > a) or (y >= 4))):
                flag = False
                break
        if not flag:
            break
    if flag:
        count += 1
print(count)