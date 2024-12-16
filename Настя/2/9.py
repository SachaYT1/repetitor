f = open('9 (5).txt').readlines()
count = 0
for i in f:
    a = list(map(int, i.split()))
    count_plus = 0
    count_minus = 0
    max_plus = -10**6
    min_minus = 10**6
    for num in a:
        if num < 0:
            count_minus += 1
            if num < min_minus:
                min_minus = num
        elif num > 0:
            count_plus += 1
            if num > max_plus:
                max_plus = num

    if (count_minus > 0 and count_plus > 0) and (count_minus > count_plus) and (abs(min_minus) > max_plus):
        count += 1
print(count)