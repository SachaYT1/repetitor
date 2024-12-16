a =[]
for x in range(0, 18 + 1):
    alphabet = ['0', '1', '2', '3', '4', '5','6','7', '8','9','A','B','C','D','E','F','G','H', 'I']
    num1 = f'98897{alphabet[x]}21'
    num2 = f'2{alphabet[x]}923'
    equation = int(num1, 19) + int(num2, 19)
    if equation % 18 == 0:
        a.append(equation // 18)
print(max(a))