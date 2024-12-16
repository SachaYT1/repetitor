def perevod(num):
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'
                ,'J', 'K', 'L', 'M', 'N', 'O']
    num_25 = ''
    while num > 0:
        num_25 = alphabet[num % 25] + num_25
        num //= 25
    return num_25

num = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2025

print(perevod(num))
print(perevod(num).count('0'))