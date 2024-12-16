f = open('9_3.txt').readlines()
count = 0
for i in f:
    a = list(map(int, i.split()))
    a.sort()
    evenNumbers = []
    for elem in a:
        if elem % 2 == 0:
            evenNumbers.append(elem)
    secondMax = a[-2]
    secondMin = a[1]
    if len(evenNumbers) > 0:
        if sum(evenNumbers) / len(evenNumbers) > (secondMin + secondMax) / 2:
            count += 1
print(count)