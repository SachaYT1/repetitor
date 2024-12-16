f = open('24_2426.txt').read()
a = ['1', '2', '3']
b = []
for i in range(ord('0'), ord('9') + 1):
    b.append(chr(i))
print(b)

c = 0
c_max = 0
for letter in f:
    if letter in a:
        c += 1
        if c > c_max:
            c_max = c
    else:
        c = 0
print(c_max)
