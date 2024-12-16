f = open('24-157.txt', 'r').readline()
alphabet = [0] * 26
# ord('A') == 65

for i in range(len(f) - 2):
    if f[i] == f[i + 1]:
        alphabet[ord(f[i + 2]) - 65] += 1

countMax = -1
letter = ''
for count in range(len(alphabet)):
    if alphabet[count] > countMax:
        letter = chr(count + 65)
        countMax = alphabet[count]


print(letter, countMax)
