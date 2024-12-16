for n in range(131, 256):
    n_2 = bin(n)[2:]
    n_2 = (8 - len(n_2)) * '0' + n_2
    n_2 = n_2[0] + n_2[1] + n_2[6] + n_2[7]
    r = int(n_2, 2)
    if r == 10:
        print(n)
        break