# product - делает все возможные комбинации учитывая повторения
# permutations - без повторени
from itertools import product, permutations

# не забываем, что иногда нужно в алфавитном порядке, лайфхак смотрим на последние буквы в примере
# product - repeat, permutations - r :: количество букв в слове
a = product('...', repeat=...)
n = 1
ans = 0
for i in a:
    s = ''.join(i)
    # какое-то условие
    if s.count('.') == ... and len(set(s)) == ...:
        ans = n
    n += 1
print(ans)




a = permutations('0123456789ABCDEF', r=4)
ans = 0
for i in a:
    s = ''.join(i)
    chet = ['0', '2', '4', '6', '8', 'A', 'C', 'E']
    countChet = 0
    summaChet = 0
    summaNechet = 0

    # вот это очень важно !!
    #
    if s[0] != '0':
        for j in s:
            if j in chet:
                countChet += 1
                summaChet += int(j, 16)
            else:
                summaNechet += int(j, 16)
        if countChet == 2 and summaChet == summaNechet:
            ans += 1
print(ans)




# что-то на сложном
from itertools import product
a = product('ГИПЕРБОЛА', repeat=6)
count = 0
count1 = 0
for i in a:
    s = ''.join(i)
    glas = ['И', 'Е', 'О', 'А']
    soglas = ['Г', 'П', 'Р', 'Б', 'Л']

    if s[0] not in glas and s[-1] not in glas:
        count += 1
        flag = True
        for j in range(1, len(s) - 1):
            if s[j] in glas:
                if s[j - 1] in soglas and s[j + 1] in soglas:
                    count -= 1
                    flag = False
                    break
        if flag:
            count1 += 1

print(count1)
