from itertools import permutations

a = permutations('02468ACE')
count = 0
for i in a:
    s = ''.join(i)

