a = input()
print(a)

b = "настя"

if a == b:
    print("УРА")
else:
    print(":(")

countA = 0
countNotA = 0
for i in range(0, len(a)):
    if a[i] == "а":
        countA += 1
    else:
        countNotA += 1
print(countNotA)

c = 'самолёт'
c_new = c[2:len(c)-2]
print(c_new)
