f = open('9 (7).txt').readlines()

count = 0
for i in f:
    a = list(map(int, i.split()))
    b=set(a)
    nechet = 0
    chet = 0
    c = 1
    n = 0
    for num in a:
        if num % 2 == 0:
            chet += 1
            c *= num
        else:
            nechet += 1
            n += num
    if chet >= 2 and nechet >= 2 and n*3 > c:
        count += 1

print(count)