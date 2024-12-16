f = open('24-153.txt', 'r').readline()

a = f.split('D')
minLen = 10 ** 7

for j in a:
    minLen = min(len(j), minLen)
print(minLen + 2)