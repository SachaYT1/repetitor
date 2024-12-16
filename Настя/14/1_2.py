def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base

def sumInString(num):
    ans = 0
    for elem in num:
        ans += int(elem)
    return ans


num = 51 * 7 ** 12 - 7 ** 3 - 22
print(sumInString(perevod(num, 7)))