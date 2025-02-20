for n in range(3, 10001):
    a = '8' + '4' * n
    while ('4444' in a) or ('844' in a) or ('84' in a):
        if '4444' in a:
            a = a.replace('4444', '884', 1)
        if '844' in a:
            a = a.replace('844', '488', 1)
        if '84' in a:
            a = a.replace('84', '3343', 1)
    if len(a) >= 20:
        print(n, len(a))
    