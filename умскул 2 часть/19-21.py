def Win1(x, S):
    return (x * S < 75) and (((x + 3) * S >= 75) or ((S + 3) * x >= 75) or ((x + 4) * S >= 75) or ((S + 4) * x >= 75))


def Loss1(x, S):
    return (not (Win1(x, S))) and (Win1(x + 3, S) or Win1(x, S + 3) or Win1(x + 4, S) or Win1(x, S + 4))


def Win2(x, S):
    return Loss1(x + 3, S) or Loss1(x, S + 3) or Loss1(x + 4, S) or Loss1(x, S + 4)


def Loss12(x, S):
    return ((Win1(x + 3, S) or Win2(x + 3, S)) and (Win1(x, S + 3) or Win2(x, S + 3)) and
            (Win1(x + 4, S) or Win2(x + 4, S)) and (Win1(x, S + 4) or Win2(x, S + 4)) and
            (Win2(x + 3, S) or Win2(x, S + 3) or Win1(x + 4, S) or Win1(x, S + 4)))


x = 1
S19 = []
for S in range(1, 75):
    if Win1(x + 3, S) or Win1(x, S + 3) or Win1(x + 4, S) or Win1(x, S + 4):
        S19.append(S)
print(min(S19))

x = 1
S20 = []
for S in range(1, 75):
    if Win2(x, S):
        S20.append(S)
S20.sort()
print(S20[0], S20[-1])

x = 1
S21 = []
for S in range(1, 75):
    if Loss12(x, S):
        S21.append(S)
print(min(S21))
