f = open('24 (4).txt').readline().strip()
f = f.replace('A', '@A').replace('D', 'D@')
s = f.split('@')
print(s)
len_str = 0
max_len = 0
for i in s:
    if len(i) > 2:
        if i[0] == 'A' and i[-1] == 'D':
            len_str = len(i) - 2
        else:
            len_str = 0
        max_len = max(max_len, len_str)
print(max_len)
