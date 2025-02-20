f = open('1.txt').read()
s = f.split('E')
ans = 0
for i in range(1, len(s) - 1):
    string = s[i]
    flag = True
    for letter in string:
        if not(letter == 'D' or letter == 'N'):
            flag = False
            break
    if flag:
        ans = max(ans, len(string) + 2)
print(ans)