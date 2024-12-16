f = open('26.10.test')
n, m = map(int, f.readline().split())

boxes = []
ribbons = []
c = 0
while c < m:
    lenOfBox, lenOfRibbon = map(int, f.readline().split())
    boxes.append(lenOfBox)
    ribbons.append(lenOfRibbon)
    c += 1

c = 0
while c < n - m:
    lenOfBox = int(f.readline())
    boxes.append(lenOfBox)
    c += 1

boxes.sort(reverse=True)
ribbons.sort(reverse=True)


ans = []
x = -1
for c in range(0, len(boxes)):
    if boxes[c] in ribbons:
        ans = [boxes[c]]
        x = boxes[c]
        break

minim = 10 ** 9
for i in range(1, len(boxes)):
    if (x - boxes[i]) >= 7 and boxes[i] in ribbons:
        ans.append(boxes[i])
        x = boxes[i]

print(len(ans), ans[0] - ans[-1])
