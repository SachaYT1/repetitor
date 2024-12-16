f = open('9_11228.txt').readlines()

summ = 0
for i in f:
    a = list(map(int, i.split()))
    a.sort()
    k3 = set([elem for elem in a if a.count(elem) == 3])
    k2 = set([elem for elem in a if a.count(elem) == 2])
    if len(k3) == 1 and len(k2) == 2:
        ost = [num % 2 for num in a[:4]]
        if ost.count(1) == 2:
            summ += sum(a)
print(summ)