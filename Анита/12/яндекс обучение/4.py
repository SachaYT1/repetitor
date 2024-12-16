s = '3' * 50 + '6' * 50 + '9' * 50

while '63' in s or '69' in s or '93' in s:
    s = s.replace('63', '36', 1)
    s = s.replace('69', '96', 1)
    s = s.replace('93', '39', 1)

print(s[41], s[99], s[143])
print(s)