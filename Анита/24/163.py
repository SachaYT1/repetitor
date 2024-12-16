f = open('24-s1.txt').readlines()

maxAlphabetPairs = -1
minLetter = ''
for s in f:
    alphabetPairs = 0
    for i in range(len(s) - 1):
        if ord(s[i]) == ord(s[i + 1]) - 1:
            alphabetPairs += 1
    if alphabetPairs >= maxAlphabetPairs:
        maxAlphabetPairs = alphabetPairs
        minCountLetter = 10 ** 6
        letter = ''
        for elem in range(ord('A'), ord('Z') + 1):
            if s.count(chr(elem)) < minCountLetter:
                minCountLetter = s.count(chr(elem))
                minLetter = chr(elem)

countLetter = 0
for s in f:
    countLetter += s.count(minLetter)


print(minLetter, countLetter)
