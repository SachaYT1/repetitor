f = open('KGE_24_17563.txt').read()

f = f.replace('--', '- -').replace('**', '* *').replace('*-', '* -').replace('-*', '- *')
a = f.split()
for equation in a:
    equation = equation.strip('*-')
    print(equation)
    break


print(str(int('000000345')))
print('0-089-70')
print('0   89-70')

print(str(int('0')))