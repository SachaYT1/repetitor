from itertools import permutations
a = permutations('ННННЧЧЧЧЧЧЧ', r=11)
ans_start_with_even = set()
ans_start_with_odd = set()
for i in a:
    s = ''.join(i)
    if 'НН' not in s:
        if s[0] == 'Ч':
            ans_start_with_even.add(s)
        else:
            ans_start_with_odd.add(s)
print(len(ans_start_with_even) * (3 * 4 ** 10) + len(ans_start_with_odd) * (4 ** 11))