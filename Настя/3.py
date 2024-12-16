str1 = input()
str2 = input()

glasn = 'АЕЁОИЭЯЮЫ'

count_glasn = 0
count_soglasn = 0

for i in range(len(str1)):
    bukva = str1[i]
    if bukva in glasn:
        count_glasn += 1

for i in range(len(str2)):
    bukva = str2[i]
    if bukva not in glasn:
        count_soglasn += 1

if count_glasn == count_soglasn:
    print('УРа')
else:
    if str1 == str2[::-1]:
        print('Палиндромы')


num = -m