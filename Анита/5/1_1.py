def decimalToAnyBase(num, base):
    num_base = ''
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
    while num > 0:
        if num % base >= 10:
            num_base = alphabet[num % base - 10] + num_base
        else:
            num_base = str(num % base) + num_base
        num //= base
    return num_base


