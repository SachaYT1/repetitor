def perevod(num, base):
    num_base = ''
    a = set()
    while num > 0:
        a.add(num % base)
        # num_base = str(num % base) + num_base
        num //= base
    return len(a)

num = 4326546456
print(perevod(num, 15))


