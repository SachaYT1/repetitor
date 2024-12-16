f = open('24-j6.txt', 'r').readline()
countIncreasingSequenceLen5 = 0
lenIncreasingSequence = 1
increasingSequence = f[0]

for i in range(1, len(f)):
    if f[i] > f[i -1]:
        increasingSequence += f[i]
        lenIncreasingSequence += 1
    else:
        if lenIncreasingSequence == 5:
            countIncreasingSequenceLen5 += 1
        increasingSequence = f[i]
        lenIncreasingSequence = 1
print(countIncreasingSequenceLen5)


