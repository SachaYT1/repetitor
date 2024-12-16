alphabet = []
for i in range(ord('0'), ord('9') + 1):
    alphabet.append(chr(i))
for i in range(ord('A'), ord('Z') + 1):
    alphabet.append(chr(i))


def perevod(num, base):
    num_base = ''
    while (num > 0):
        num_base = alphabet[num % base] + num_base
        num //= base
    return num_base

count =0
for x in range(0, 625):
    if len(perevod(x, 2)) >= 5 and perevod(x, 16)[-1] == 'C':
        count += 1
print(count)