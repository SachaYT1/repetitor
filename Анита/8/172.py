from itertools import product
a = product('СОЛОВЕЙ', repeat=6)
ans = set()
count = 0
for i in a:
    s = ''.join(i)
    if s.count('Й') <= 1 and (s[0] != 'Й' and 'Й' != s[-1] and 'ЙЕ' not in s and 'ЕЙ' not in s):
        count += 1
        ans.add(s)
print(count)
print(len(ans))
