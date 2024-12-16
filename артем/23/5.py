a = []

def f(x):
    if x > 100:
        return 0
    elif x % 2 == 1:
        a.append(x)

    return f(x + 3) + f(x * 3)

print(f(10))
print(a)
print(len(set(a)))