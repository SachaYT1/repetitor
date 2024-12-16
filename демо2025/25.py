def find_divisors(n):
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # проверяем, чтобы не добавить квадратный корень дважды
                divisors.append(n // i)
            break
    return divisors

def find_m(n):
    divisors = find_divisors(n)
    if divisors:
        return min(divisors) + max(divisors)
    else:
        return 0

count = 0
n = 800001
while count < 5:
    m = find_m(n)
    if m % 10 == 4:
        print(f"{n} | {m}")
        count += 1
    n += 1
