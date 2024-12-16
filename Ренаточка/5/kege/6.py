
n_2 = '0001'
print(int(n_2, 2))
stroka = 'sasha+renata'
print(stroka[::-1])


for n in range(1, 100 + 1):
    n_2 = bin(n)[2:]
    n_2 = n_2[::-1]

    if int(n_2, 2) == 13:
        print(n)

