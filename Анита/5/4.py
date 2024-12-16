digits = []
for digit in str(433):
    digits.append(digit)

print('анита'[-2:])

for num in range(100, 999 + 1):
    digits = [digit for digit in str(num)]
    digits.sort()
    print(digits)
    max_num = int(digits[2] + digits[1])
    if digits[0] == '0':
        min_num = int(digits[1] + digits[0])
    else:
        min_num = int(digits[0] + digits[1])

    if max_num - min_num == 60:
        print(num)
        break