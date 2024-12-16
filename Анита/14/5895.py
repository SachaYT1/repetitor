ans = set()
for y in range(2, 16):
    for x in range(y):
        num1 = 12 + y * 16 + x * 16 ** 2 + 5 * 16 ** 3
        num2 = 7 + x * y + x * y ** 2 + 8 * y ** 3
        s = num2 + num1
        ans.add(s)
print(len(ans))