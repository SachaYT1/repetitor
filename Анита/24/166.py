f = open('24-164.txt').readlines()

maxDistant = -10**7
for s in f:
    if s.count('G') < 15:
        indexesOfEqualLetters = []
        for letter in range(ord('A'), ord('Z') + 1):
            indexesOfEqualLetters.append([s.find(chr(letter)), s.rfind(chr(letter))])
        for arr in indexesOfEqualLetters:
            maxDistant = max(arr[1] - arr[0], maxDistant)
print(maxDistant)