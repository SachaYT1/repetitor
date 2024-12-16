a = []
for n in range(2, 13):
    n_2 = bin(n)[2:]
    if n % 2 == 0:
        n_2 += '10'
    else:
        n_2 = '1' + n_2 + '01'
    
    r = int(n_2, 2)
    a.append(r)
print(max(a))