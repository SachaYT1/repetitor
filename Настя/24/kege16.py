f = open('24_9552.txt').read()

# while 'BB' in f:
f = f.replace('PCSGO', 'PC CSGO')
# while 'DD' in f:
f = f.replace('PC', '*').replace('CSGO', '+')

for i in range(ord('A'), ord('Z') + 1):
    f = f.replace(chr(i), ' ')


s = f.split()
c_max = 0
for string in s:
    c = 0
    for symbol in string:
        if symbol == '+':
            c += 4
        elif symbol == '*':
            c += 2
    if c > c_max:
        c_max = c

print(c_max)