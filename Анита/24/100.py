f = open('24-2.txt', 'r').readline()
maxIncreasingSequence = f[0]
increasingSequence = f[0]
for i in range(len(f) - 1):
    if f[i] < f[i + 1]:
        increasingSequence += f[i + 1]
        if len(increasingSequence) > len(maxIncreasingSequence):
            maxIncreasingSequence = increasingSequence
    else:
        increasingSequence = f[i + 1]  # explain why f[i + 1]
print(maxIncreasingSequence)
