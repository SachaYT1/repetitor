f = open('digits1.txt').read()

alphabet = []
for i in range(ord('0'), ord('9') + 1):
    alphabet.append(chr(i))


for i in range(ord('A'), ord('E') + 1):
    alphabet.append(chr(i))

# a = 'Z'
# print(ord(a))
# print(chr(89))

m = ''
maxNum = 0
ans = 0
for i in range(len(f)):
    char = f[i]
    if char in alphabet and not(char == '0' and m == ''): 
        m += char
        if int(m, 15) % 5 == 0:
            if int(m, 15) > maxNum:
                maxNum = int(m, 15)
                ans = i
    else:
        m = ''

print(ans)