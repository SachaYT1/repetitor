f = open('k8-0.txt', 'r').readline()
k = 1
k_max = 1
k_max_symbol = ''

for i in range(len(f) - 1):
    if f[i] == f[i + 1]:
        k += 1
        if k > k_max:
            k_max = k
            k_max_symbol = f[i]
    else:
        k = 1

print(k_max_symbol, k_max)