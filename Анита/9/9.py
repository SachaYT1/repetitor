f = open('9 (2).txt').readlines()
count = 0
for i in f:
    a = list(map(int, i.split()))
    b = set(a)
    sumWithoutMax = sum(a) - max(a)
    if (len(a) == len(b) and not(max(a) > sumWithoutMax)) or (not(len(a) == len(b)) and (max(a) > sumWithoutMax)):
        count += 1
print(count)


