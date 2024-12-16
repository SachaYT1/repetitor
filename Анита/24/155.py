f = open('24-153.txt', 'r').readline()

indexA = -1
minLenSequenceAF = 10 ** 7
lenSequenceAF = 0
for i in range(len(f)):
    if f[i] == 'A':
        indexA = i
    elif f[i] == 'F' and indexA > -1:
        lenSequenceAF = i - indexA + 1
        if lenSequenceAF != 2:
            minLenSequenceAF = min(lenSequenceAF, minLenSequenceAF)

print(minLenSequenceAF)