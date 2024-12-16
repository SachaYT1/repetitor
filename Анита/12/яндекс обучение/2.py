def sumDigitsInString(string):
    ans = 0
    for digit in string:
        ans += int(digit)
    return ans


for m in range(1, 1000):
    s = '4' + m * '6'

    while '46' in s or '666' in s:
        s = s.replace('46', '5', 1)
        s = s.replace('666', '4 ', 1)

    if sumDigitsInString(s) > 1000:
        print(m)
        break
