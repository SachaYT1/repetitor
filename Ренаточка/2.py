def sumDigitsInString(string):    ans = 0
    for digit in string:        ans += int(digit)
    return ansk = 0
for n in range(100000000, 1000000000):    num = sumDigitsInString(str(n))
    b = bin(num)[2:]    if sumDigitsInString(b) % 2 == 0:
        b = '1' + b + '00'    else:
        b = '10' + b + '1'    r = int(b, 2)
    if r == 21:        k += 1
print(k)