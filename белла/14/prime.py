def prime_numbers(num):
    flag = True
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            flag = False
            break
    if flag:
        return True
    else:
        return False


print(prime_numbers(13))
print(prime_numbers(234))