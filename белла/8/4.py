from itertools import product
a = product('АЙЛМ', repeat=5)
count = 0
ans = 0
for i in a:
    s = ''.join(i)
    count += 1
    if s.count('М') <= 1 and ('ЛЛ' not in s):
        ans = count
print(ans)
        