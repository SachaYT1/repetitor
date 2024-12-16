def perevod(num, base):
    num_base = ''
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    while num > 0:
        if num % base >= 10:
            num_base = alphabet[num % base - 10] + num_base
        else:
            num_base = str(num % base) + num_base
        num //= base
    return num_base



for x in range(4, 20):
    num1 = int('21', x)
    num2 = int('13', x)
    num3 = int('313', x)

    if num1 * num2 == num3:
        print(x)
