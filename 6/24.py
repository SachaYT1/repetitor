for y in range(7, 10):
    for x in range(0, y):
        num1 = f'4163{x}1'
        num_1_perevod = int(num1, y)
        if num_1_perevod == 247393:
            print(x, y)


alphabet = []
for num in range(0, 10):
    alphabet.append(str(num))
for u in range(ord('A'), ord('Z')):
    alphabet.append(chr(u))
print(alphabet)
