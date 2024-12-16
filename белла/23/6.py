ans = set()
def f(x):
    if x >= 100:
        return 0
    if x % 2 == 1:
        ans.add(x)
    return f(x + 3) + f(x * 3)

f(10)
print(len(ans))