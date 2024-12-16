f = open('24_1975.txt').read()
c = 0
c_max = 0
prev_letter = ''
for letter in f:
    if prev_letter == 'P' and letter == 'P':
        c = 1
    else:
        c += 1
        if c > c_max:
            c_max = c

    prev_letter = letter
print(c_max)