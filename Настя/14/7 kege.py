def perevod(num, base):
    num_base = ''
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
    while num > 0:
        num_base = alphabet[num % base] + num_base
        num //= base
    return num_base

num = 6 * 144 ** 26 + 11 * 12 ** 75 - 48
num_12 = perevod(num, 12)
print(num_12.count('B'))

