for x in range(0, 15 + 1):
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
    num1 = f'9897{alphabet[x]}21'
    num2 = f'12{alphabet[x]}023'
    result = int(num1, 15) + int(num2, 15)
    if result % 14 == 0:
        print(result // 14)
        break
