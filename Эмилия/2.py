


for a in range(1000, 10000):
    sA = str(a)
    summaChet = 0
    digits = []

    for digit in sA:
        digits.append(int(digit))
        
    for num in digits:
        if num % 2 == 0:
            summaChet += num


    maxNum = max(digits)
    minNum = min(digits)
    diff = (maxNum - minNum) ** 3
    summaChet = summaChet ** 2

    ans = ''
    if diff >= summaChet:
        ans = str(summaChet) + str(diff)
    else:
        ans = str(diff) + str(summaChet)

    if ans == '4343':
        print(a)
        break





