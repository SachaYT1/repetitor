# ну это классика, максимально шаблонная задачка, бывают ещё 2 переменные, но это просто ещё один цикл
for a in range (1, 1000):
    flag = True
    for x in range(1, 100):
        f = not((x & 26 != 0) or (x & 13 != 0)) or (not(x & 29 == 0) or (x & a != 0))
        if not f:
            flag = False
            break
    if flag:
        print(a)
        break


# пример решения множеств - хз, мне больше нравится руками, но тут как пойдет, иногда не очень очевиднор как написать код
a = set()
for i in range(1, 1000):
    a.add(i)
d = set()
b = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
c = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
for x in range(1, 1000):
    f = (not(x in a) or (x in b)) and (not(x in c) or not(x in a))
    if f:
        d.add(x)
print(d)


# и решение отрезков - такая же ситуация, я бы все равно решил руками, потому что предпологается что нужно решать НЕ кодом
min_len = 10**9
for l in range(1, 500):
    for r in range(l + 1, 500):
        flag = True
        for i in range(2, 500):
            x = i / 2
            f = not(17 <= x <= 58) or (not(not(29 <= x <= 80) and not(l <= x <= r)) or not(17 <= x <= 58))
            if not f:
                flag = False
                break
        if flag:
            min_len = min(min_len, r - l)

print(min_len)