s = open('24AD.txt').readline()
indexA = s.find('A')
indexD = s.find('D')
len_str = m = 0
str1 = ''
for i in range(min(indexD, indexA)+1, len(s)):
    if s[i] == 'A':
        if indexA < indexD:
            len_str = i - indexD + 1
            m = max(len_str, m)
        indexA = i
    if s[i] == 'D':
        if indexD < indexA:
            len_str = i - indexA + 1
            if len_str > m:
                m = max(len_str, m)
        indexD = i
print(m)