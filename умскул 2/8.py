from itertools import product

a = product('СЕРГЕЙ', repeat=5)
ans = set()
for i in a:
    s = "".join(i)
    if s[0] != 'Й' and 'ЕЙ' not in s and 'ЙЕ' not in s and s.count('Й') <= 1:
        ans.add(s)
print(ans)
print(len(ans))