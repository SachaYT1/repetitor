f = open('17.txt').readlines()
r = []
for a in f:
    r.append(int(a))

min2025 = 10**10
for num in r:
    if num % 2025 == 0:
        min2025 = min(min2025, num)

print(min2025)
ans = 0
maxsim = -11111111
for i in range(len(r)-2):
    num1 = r[i]
    num2 = r[i+1]
    num3 = r[i+2]
    if 100000 <= (num1 + num2 + num3) <= 999999:
        if (num1 % min2025 == 0) + (num2 % min2025 == 0) + (num3 % min2025 == 0) >= 1:
            ans += 1
            maxsim = max(maxsim, (num1 + num2 + num3))

print(ans, maxsim)