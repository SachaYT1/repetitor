def task19():
    def f(s1, s2, c, m):
        if s1 * s2 >= 75:
            return c % 2 == m % 2
        if c == m:
            return 0

        h = [f(s1 + 3, s2, c + 1, m), f(s1, s2 + 3, c + 1, m), f(s1 + 4, s2, c + 1, m), f(s1, s2 + 4, c + 1, m)]

        return any(h) if (c + 1) % 2 == m % 2 else any(h)

    ans = []
    for s2 in range(1, 74 + 1):
        for m in range(5):
            if f(1, s2, 0, m):
                if m == 2:
                    ans.append(s2)
                break

    print(min(ans))


def task20():
    def f(s1, s2, c, m):
        if s1 * s2 >= 75:
            return c % 2 == m % 2
        if c == m:
            return 0

        h = [f(s1 + 3, s2, c + 1, m), f(s1, s2 + 3, c + 1, m), f(s1 + 4, s2, c + 1, m), f(s1, s2 + 4, c + 1, m)]

        return any(h) if (c + 1) % 2 == m % 2 else all(h)

    ans = []
    for s2 in range(1, 74 + 1):
        for m in range(5):
            if f(1, s2, 0, m):
                if m == 3:
                    ans.append(s2)
                break
    ans.sort()
    print(f'{ans[0]}{ans[-1]}')


def task21():
    def f(s1, s2, c, m):
        if s1 * s2 >= 75:
            return c % 2 == m % 2
        if c == m:
            return 0

        h = [f(s1 + 3, s2, c + 1, m), f(s1, s2 + 3, c + 1, m), f(s1 + 4, s2, c + 1, m), f(s1, s2 + 4, c + 1, m)]

        return any(h) if (c + 1) % 2 == m % 2 else all(h)

    ans = []
    for s2 in range(1, 74 + 1):
        for m in range(5):
            if f(1, s2, 0, m):
                if m == 4:
                    ans.append(s2)
                break
    print(min(ans))


# вызовите функции задачи, которую хотите решить, по примеру снизу
task19()
task20()
task21()
