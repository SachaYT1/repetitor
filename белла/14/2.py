alphabet = []
for i in range(ord('0'), ord('9') + 1):
    alphabet.append(chr(i))
for i in range(ord('A'), ord('Z') + 1):
    alphabet.append(chr(i))
print(alphabet)

for x in range(0, 14 + 1):
    num = 1 * 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5
    num1 = int(f'123{alphabet[x]}5', 15)
    num2 = int(f'1{alphabet[x]}233', 15)
    if (num1 + num2) % 14 == 0:
        print((num1 + num2) // 14)

