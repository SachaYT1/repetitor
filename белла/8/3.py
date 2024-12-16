from itertools import product
a = product('БАНДЕРОЛЬ', repeat=7)
for i in a:
    s = ''.join(i)
    if s.count('Ь') <= 1 and ('ДЕ' not in s) and ('ЕД' not in s)
        ('ДЕ' not in s) and 