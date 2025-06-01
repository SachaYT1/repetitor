print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                '''
                какая-то функция
                ∧ - and, ∨ - or, & (конъюкция) пишем так же
                a -> b - импликация (not a or b)
                just in case - https://studfile.net/preview/2967993/          
                '''

                f = ...
                # f = (((not x) and y) == z) and w


                # 1 - true, 0 - false
                if f == 1:
                    print(x, y, z, w)
