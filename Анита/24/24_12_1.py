f = open('24_8654.txt').readlines()
maxCountExE = -1
letter = ''
for s in f:
    countExE = 0
    for i in range(len(s) - 2):
        if s[i] == 'E' and s[i + 2] == 'E':
            countExE += 1

    if countExE > maxCountExE:
        maxCountExE = countExE
        minCountLetter = 10 ** 9

        countR = s.count('R')
        if countR != 0 and countR < minCountLetter:
            minCountLetter = countR
            letter = 'R'

        countT = s.count('T')
        if countT != 0 and countT < minCountLetter:
            minCountLetter = countT
            letter = 'T'

        countY = s.count('Y')
        if countY != 0 and countY < minCountLetter:
            minCountLetter = countY
            letter = 'Y'

countLetter = 0
for s in f:
    countLetter += s.count(letter)
print(countLetter)
