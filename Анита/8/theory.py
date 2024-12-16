from itertools import product, permutations


b = product('СОЛОВЕЙ', repeat=6)
count = 0
ans = set()
for i in b:
    s = ''.join(i)
    if s.count('Й') <= 1 and (s[0] != 'Й' and 'Й' != s[-1] and 'ЙЕ' not in s and 'ЕЙ' not in s):
        count += 1
        ans.add(s)
print(len(ans))
