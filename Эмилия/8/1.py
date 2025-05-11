from itertools import product, permutations 


b = product('КРЕСЛО', repeat=4)

k = 0
for i in b:
    s = "".join(i)
    if s[0] in 'КРСЛ' and s[3] in 'ЕО':
        k += 1
print(k)

