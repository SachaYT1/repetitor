def deliteli(num):
    ans = set()
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            ans.add(i)
            ans.add(num // i)
    return ans 

k = 0
for num in range(150001, 10**6):
    s = sum(deliteli(num))
    if s % 13 == 10:
        print(num, s)
        k += 1
    if k == 7:
        break