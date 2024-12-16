def decimalToAny(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    if num_base == '':
        return '0'
    return num_base

