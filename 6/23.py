for x in range(0, 15):
    for y in range(0, 17):
        alphabet = ['0', '1', '2', '3', '4', '5', '6',
                    '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
        num1 = f'123{alphabet[x]}5'
        num2 = f'67{alphabet[y]}9'
        eq = int(num1, 15) + int(num2, 17)
        if eq % 131 == 0:
            print(eq // 131)
            print(x, y)