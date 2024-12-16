alphabet = []
for i in range(ord('0'), ord('9') + 1):
    alphabet.append(chr(i))
for i in range(ord('A'), ord('Z') + 1):
    alphabet.append(chr(i))


for x in range(21):
    flag = True
    eq = 0
    for y in range(21):
        num1 = int(f'12{alphabet[y]}{alphabet[x]}9', 21)
        num2 = int(f'36{alphabet[y]}99', 21)
        if (num1 + num2) % 18 != 0:
            flag = False
            break
        if y == 5:
            eq = (num1 + num2) // 18
    if flag:
        print(eq)
        break

