f = open('24_2420 (1).txt').read()
a = ['A', 'B', 'E', 'F']
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