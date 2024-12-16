f = open('24-174.txt').readlines()
count = 0
maxLength = 0
for s in f:
    if s.count('R') < 30:
        for letterOrd in range(ord('A'), ord('Z') + 1):
            index1 = s.find(chr(letterOrd))
            index2 = 0
            length = 0
            for i in range(index1 + 1, len(s)):
                if s[i] == chr(letterOrd):
                    index2 = i
                    length = index2 - index1
                    index1 = index2
                    if length >= 2:
                        maxLength = max(maxLength, length)
                        count += 1
print(maxLength, count)

