f = open('24-1.txt', 'r').readline()
indexFirstLocalMax = 1
indexSecondLocalMax = 1
diff = 0
diffMax = 0


for i in range(1, len(f) - 1):
    if f[i] > f[i - 1] and f[i] > f[i + 1]:
        indexSecondLocalMax = i
        diff = indexSecondLocalMax - indexFirstLocalMax
        diffMax = max(diff, diffMax)
        indexFirstLocalMax = indexSecondLocalMax
print(diffMax)
