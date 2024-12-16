f = open('demo_2025_24.txt')
s = f.read().strip()
s = s.replace('-', '*')
a = s.split('*')

st = ''
kmax = 0

for i in range(len(a)):
    # проверяем что два знака не идут подряд и первый символ не 0 (если это не единственная цифра)
    if (a[i] != '') and ((a[i][0] != '0') or (a[i] == '0')):
        if st != '':
            # восстанавливаем строку, добавляя знак
            st += '*' + a[i]
        else:
            st += a[i]
        if st.find('*') != -1:
            kmax = max(kmax, len(st))
    else:
        # убирает ведущие 0, но они не считаются в последовательности, по факту - код ради кода
        # if a[i] != '' and a[i][0] == '0':
        #     if a[i].count('0') != len(a[i]):
        #         a[i] = a[i].lstrip('0')
        #     else:
        #         a[i] = '0'
        #     st = a[i]
        #     print(st)
        # else:
        st = ''

print(kmax)
