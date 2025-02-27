for base in range(30, 36 + 1):
    num = int('LANCELOT', base) + int('ELSA', base) \
    - int('DRAGON', base) + int('CAT', base)
    if num % 1747 == 0:
        print(num)
        print(num // 1747)
