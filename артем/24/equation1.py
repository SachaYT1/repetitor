
f = open('equation.txt').read()

f = f.replace('++', '+ +').replace('+*', '+ *').replace('*+', '* +').replace('**', '* *')
a = f.split()
maxC = 0
maxString = ''
for equation in a:
    equation = equation.strip('+*')
    b = equation.split('+')
    c = 0
    string = ''
    for eq in b:
        if not (eq == ''):
            num = eval(eq)
            if num == 0:
                c += len(eq) + 1  
                string += eq + '+' 
            else:
                c = 0
                string = ''
            if c - 1 > maxC:
                maxString = string
            maxC = max(maxC, c - 1)
print(maxC)
print(maxString)


'2*3*4532*4'






# example = '2++3' # -> '2' '3' , .replace('++', '+ +') -> '2+ +3' -> split()  -> '2+' '+3' -> strip() -> '0' '3'
# a = '*++++++*312++*+'


# print(a.strip('+*'))