f = open('9(1).txt').readlines()

count = 0
for i in f:
    a = list(map(int, i.split()))
    b = set(a)
    c = 0
    for num in a:
        if num % 2 == 1:
            c += 1
    if (len(b) != len(a)) + (c == 3) == 1:
        count += 1
print(count)
