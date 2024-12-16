f = open('24-s1.txt', 'r').readlines()
count = 0
for s in f:
    if s.count('J') > s.count('E'):
        count += 1
print(count)