# тут тоже в целом ничего сложного, помним про функцию перевод из 5-го задания



# классная фича чтобы заполнить весь алфовит для систем > 10
alphabet = []
for i in range(ord('0'), ord('9') + 1):
    alphabet.append(chr(i))
for i in range(ord('A'), ord('Z') + 1):
    alphabet.append(chr(i))


for x in range(0, 14 + 1):
    # два примера как перевести числа, имхо мне нравится второй 
    num = 1 * 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5
    num1 = int(f'123{alphabet[x]}5', 15)


    num2 = int(f'1{alphabet[x]}233', 15)
    if (num1 + num2) % 14 == 0:
        print((num1 + num2) // 14)


# в целом это ещё достаточно сложный пример с двумя неизвестными
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

