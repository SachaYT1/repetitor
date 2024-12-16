def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num = num // base
    return num_base


def sumInString(string):
    a = 0
    for digit in string:
        a += int(digit)
    return a

ans = []
for n in range(1, 10000):
    n_3 = perevod(n, 3)
    if len(n_3) % 2 == 1:
        n_3 = '1' + n_3
    if sumInString(n_3) % 2 == 0:
        n_3 = n_3 + n_3[0] + n_3[1]
    else:
        n_3 = n_3 + perevod(n % 5, 3)
    if n_3[0] == '2':
        n_3 = str(int(n_3[1:]))
    if len(n_3) > 1:
        if n_3[-1] == n_3[-2]:
            n_3 = n_3[:-1]
    r = int(n_3, 3)
    if r > 150:
        ans.append(r)
print(min(ans))

