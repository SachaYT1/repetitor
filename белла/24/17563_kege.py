f = open('KGE_24_17563.txt').read()

f = f.replace('*-', '* -').replace('**', '* *').replace('-*', '- *').replace('--', '- -')

a = f.split()
ans = 0
ansString = ''
for expression in a:
    expression = expression.strip('*-')
    # print(expression)
    c = 0
    string = ''
    b = expression.replace('-', '*').split('*')
    for equation in b:
        if equation != '':
            if str(int(equation)) == equation and (equation != '0'):
                c += len(equation) + 1
                string += equation + '-'
            else:
                if equation == '0':
                    c = 2
                else:
                    c = len(str(int(equation))) + 1
                string += equation + '-'
            if c - 1 > ans:
                ansString = string
            ans = max(ans, c - 1)

print(ans)




# print(f)

# print('+'.strip('+'))
# print('123*123'.split('+'))
