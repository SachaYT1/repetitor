n = 120
n = 'саша'
n = ['1', 2, [100]]



rTarget = 29



def productChet(n: int, m: int):
    p1 = 1
    for digit in str(n):
        if int(digit) % 2 == 0 and int(digit) != 0:
            p1 *= int(digit)

    for digit in str(m):
        if int(digit) % 2 == 0 and int(digit) != 0:
            p1 *= int(digit)
    
    return p1
            

def productNechet(n: int, m: int):
    p2 = 1
    for digit in str(n):
        if int(digit) % 2 == 1 and int(digit) != 0:
            p2 *= int(digit)

    for digit in str(m):
        if int(digit) % 2 == 1 and int(digit) != 0:
            p2 *= int(digit)

    return p2



for m in range(1, 10000):
    p1 = productChet(n, m)
    p2 = productNechet(n, m)
    r = abs(p1 - p2)
    if r == 29:
        print(m)
        break
