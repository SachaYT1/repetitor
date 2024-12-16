f = open('9_18549 (1).txt').readlines()

d = dict()
for i in f:
    a = list(map(int, i.split()))
    for num in a:
        if num in d.keys():
            d[num] += 1
        else:
            d[num] = 1
print(d)


for key, value in d.items():
    if value == 141:
        print(key)