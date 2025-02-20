def f(s1, s2, s3, c, m):
    if s1 + s2 + s3 >= 73:
        return c % 2 == m % 2
    if c == m:
        return 0
    
    h = [
        f(s1 + 3, s2, s3, c + 1, m), f(s1 + 13, s2, s3, c + 1, m), f(s1 + 23, s2, s3, c + 1, m), 
         f(s1, s2 + 3, s3, c + 1, m), f(s1, s2 + 13 , s3, c + 1, m), f(s1, s2 + 23, s3, c + 1, m), 
          f(s1, s2, s3 + 3, c + 1, m), f(s1, s2, s3 + 13, c + 1, m), f(s1, s2, s3 + 23, c + 1, m), 
    ]

    return any(h) if (c % 2 != m % 2) else all(h)

for s2 in range(1, 24):
    for m in range(5):
        if f(2, s2, 2 * s2, 0, m):
            if m == 4:
                print(s2) 
            break