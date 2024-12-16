count = 0
print(2**63)

def f(n):
    global count
    count += 1
    if n >= 1:
        count += 1
        f(n - 1)
        f(n - 3)
        count += 1

f(40)
print(count)
