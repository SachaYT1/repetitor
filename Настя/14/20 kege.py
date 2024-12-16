for x in range(0, 14 + 1):
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
    num1 = f'123{alphabet[x]}5'
    num2 = f'1{alphabet[x]}233'
    result = int(num1, 15) + int(num2, 15)
    if result % 14 == 0:
        print(result // 14)
        break
