from itertools import permutations

a = permutations('0123456789ABCDEF', r=4)
ans = 0
for i in a:
    s = ''.join(i)
    chet = ['0', '2', '4', '6', '8', 'A', 'C', 'E']
    countChet = 0
    summaChet = 0
    summaNechet = 0
    if s[0] != '0':
        for j in s:
            if j in chet:
                countChet += 1
                summaChet += int(j, 16)
            else:
                summaNechet += int(j, 16)
        if countChet == 2 and summaChet == summaNechet:
            ans += 1
print(ans)