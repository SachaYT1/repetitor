f = open('24-1.txt', 'r').readline()
max_odd_num = -1
numString = ''
for elem in f:
    if '0' <= elem <= '9':
        numString += elem
        if int(numString) % 2 == 1 and int(numString) > max_odd_num:
            max_odd_num = int(numString)
    else:
        numString = ''
print(max_odd_num)
