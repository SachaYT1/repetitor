from itertools import product

a = product('ЭЧПОМАК', repeat=6)
sett = set()
for i in a:
    s = "".join(i)
    if s[0] in 'ЭОА' and s[-1] in 'ЭОА' and s[0] != s[-1] and ('ЭО' not in s and 'ОЭ' not in s and 'ЭА' not in s and 'АЭ' not in s and 'АО' not in s and 'ОА' not in s):
        sett.add(s)
        print(s)
print(len(sett))