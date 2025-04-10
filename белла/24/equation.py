f = open('equation.txt').read()
s = '*+'
while '**' in f or '++' in f or '+*' in f or '*+' in f:
    f = f.replace('*+', '* +').replace('**', '* *').replace('+*', '+ *').replace('++', '+ +')

a = f.split()
ans = 0
ansString = ''
for expression in a:
    expression = expression.strip('*+')
    c = 0
    string = ''
    b = expression.split('+')
    for equation in b:
        if equation != '':
            if eval(equation) == 0:
                c += len(equation) + 1
                string += equation + '+'
                if c - 1 > ans:
                    ansString = string
                ans = max(ans, c - 1)
            else:   
                c = 0
print(ans)




# print(f)

# print('+'.strip('+'))
# print('123*123'.split('+'))