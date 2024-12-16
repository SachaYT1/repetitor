alphabet = []
for i in range(0, 10):
    alphabet.append(str(i))
for i in range(ord('A'), ord('Z') + 1):
    alphabet.append(chr(i))


for x in range(0, 22):
    for y in range(0, 13):
        num1 = f'{alphabet[x]}23{alphabet[x]}5'
        num2 = f'67{alphabet[y]}9{alphabet[y]}'
        if abs(int(num1, 22) - int(num2, 13)) % 57 == 0:
            print((int(num1, 22) - int(num2, 13)) // 57)
            print(x + y)


