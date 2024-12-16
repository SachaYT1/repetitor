from itertools import permutations
a = permutations('ЧЧЧЧЧЧЧНННН')

countCombsWith0 = set() # начинается с четной
countCombsWithout0 = set() # начинается с нечетной
for i in a:
    s = ''.join(i)
    if 'НН' not in s:
        if s[0] == 'Ч':
            countCombsWith0.add(s)
        else:
            countCombsWithout0.add(s)
ans = (4 ** 10 * 3) * len(countCombsWith0) + (4 ** 11) * len(countCombsWithout0)
print(ans)