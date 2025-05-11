from itertools import product

b = 'ЛЕМУР'
print(''.join(sorted('ЛЕМУР')))


a = product('ЕЛМРУ', repeat=4)


number = 1
for i in a:
    s = ''.join(i)

    if s[0] == 'Л' and s.count('Л') == 1:
        print(number)
        break

    number += 1

