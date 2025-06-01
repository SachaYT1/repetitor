def sumDigitsInString(a):
    b = 0
    for i in range(len(a)):
        b += int(a[i])
    return b

def perevod(num, base):
    num_base = ''
    while num > 0:
        num_base = str(num % base) + num_base
        num //= base
    return num_base



a = []

# система, указанная в условии
base = ...

for n in range(1, 10001):
    # создаем систему, которую просят
    n_base = perevod(n, base)


    # - для двоичной можно использовать
    n_2 = bin(n)[2:]
    
    # это 8 битная двоичная запись, иногда просят
    n_2 = (8 - len(n_2)) * '0' + n_2


    # перевернуть запись 
    n_base = n_base[::-1]

    # добавить что-то в конец к записи. в примере - последнюю цифру записи
    n_base = n_base + n_base[-1]

    # получаем число r - десятичная запись нашего числа
    r = int(n_base, base)

    # здесь не забываем, что не всегда break - иногда так делать нельзя!!
    # альтернатива добавить в массив и выписать min/max 
    if r > ...:
        print(n)
        a.append(r)
        break

print(min(a))



