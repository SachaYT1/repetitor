f = open('26_21424.txt')


n = int(f.readline())

boxes = []

for i in range(n):
    length = int(f.readline())
    boxes.append(length)

boxes.sort()


maxCountBox = 0
ansBox = 0
for i in range(n):
    minBox = boxes[i]
    currentBox = boxes[i]
    j = i + 1
    countBoxes = 1
    while (j < n):
        if boxes[j] - currentBox >= 9:
            countBoxes += 1
            currentBox = boxes[j]
        j += 1

    if countBoxes >= maxCountBox:
        maxCountBox = countBoxes
        if minBox > ansBox:
            ansBox = minBox
    else:
        break

print(maxCountBox, ansBox)

 