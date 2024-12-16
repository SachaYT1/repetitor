alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
for x in range(17):
    dig = alphabet[x]
    num1 = int(f'7AC{dig}53D', 17)
    num2 = int(f'83BG94{dig}D', 17)
    num3 = int(f'C5{dig}D', 17)
    num4 = int(f'C4BBF{dig}4', 17)
    num5 = int(f'7{dig}79', 17)
    summ = (num1 + num2 + num3 + num4 + num5)
    if summ % 16 == 0:
        print(summ / 16)
