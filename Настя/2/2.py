from itertools import product

a = product('02468*#', repeat=5)
count = 0
for i in a:
    s = ''.join(i)
    count_zvezda = 0
    count_reshetka = 0
    if s[0] != '0' and '*#' not in s and '#*' not in s:
        if '*' in s:
            count_zvezda += s.count('*')
        if '#' in s:
            count_reshetka += s.count('#')

        if count_reshetka > 0 and count_zvezda > 0:
            count += 5 ** count_zvezda * 4 ** count_reshetka
        elif count_reshetka > 0:
            count += 4 ** count_reshetka
        elif count_zvezda > 0:
            count += 5 ** count_zvezda
        else:
            count += 1

print(count)