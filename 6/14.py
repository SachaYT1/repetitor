for x in range(0, 15):
    alphabet = ['A', 'B', 'C', 'D', 'E']
    if x >= 10:
        num1 = f'123{alphabet[x - 10]}5'
        num2 = f'1{alphabet[x - 10]}233'
    else:
        num1 = f'123{x}5'
        num2 = f'1{x}233'
    eq = int(num1, 15) + int(num2, 15)
    if eq % 14 == 0:
        print(eq // 14)
