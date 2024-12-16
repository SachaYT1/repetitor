# страшная задачка!!
f = open('24-171.txt').readlines()

maxLength = -10 ** 7
for s in f:
    s = s.replace('XYZ', '*')
    countOfStars = 0
    indexOfLastStar = 0
    for i in range(len(s)):
        if s[i] == '*':
            countOfStars += 1
        elif s[i - 1] == '*':
            indexOfLastStar = i - 1
            indexOfFirstStar = i - countOfStars
            length = countOfStars * 3
            if s[indexOfLastStar + 1] in 'XYZ':
                length += 1
            if s[indexOfFirstStar - 1] in 'XYZ':
                length += 1
            maxLength = max(length, maxLength)
            length = 0
            countOfStars = 0

print(maxLength)
