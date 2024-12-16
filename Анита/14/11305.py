for x in '0123456789ABCDEFGHIJKLMNOPQRS':
    s = int(f'47{x}42696', 29) + int(f'8{x}22', 29)
    if s % 28 == 0:
        print(x, s // 28)
