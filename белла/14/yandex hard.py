alphabet = []
for i in range(ord('0'), ord('9') + 1):
    alphabet.append(chr(i))
for i in range(ord('A'), ord('Z') + 1):
    alphabet.append(chr(i))


ans = []
for z in range(35):
    for y in range(19):
        num1 = int(f'3B{alphabet[z]}4C', 35)
        num2 = int(f'A12F{alphabet[y]}', 19)
        if (num1 + num2) % 7 == 0:
            ans.append(z + y)
print(max(ans))
