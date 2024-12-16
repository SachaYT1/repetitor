from itertools import product, permutations


a = permutations('0234567', r=5)
count = 0
for i in a:
    s = ''.join(i)
    if s[0] != '0' and (int(s[0]) % 2 != int(s[1]) % 2) and (int(s[1]) % 2 != int(s[2]) % 2) and (int(s[2]) % 2 != int(s[3]) % 2) and \
            (int(s[3]) % 2 != int(s[4]) % 2):
        count += 1
print(count)