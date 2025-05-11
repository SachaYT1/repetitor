f = open('yandex_1.txt')
n = int(f.readline())
reqPoints = list(map(int, f.readline().split()))


students = []

for i in range(n):
    student = list(map(int, f.readline().split()))
    id = student[0]
    summaPoints = sum(student[1:])
    countZaval = 0

    for j in range(1, len(student)):
        if student[j] < reqPoints[j - 1]:
            countZaval += 1

    students.append([id, summaPoints, countZaval])


students.sort(
    key=lambda x:(
        x[2],
        -x[1],
        x[0]
    )
)


firstTask = 0
secondTask = 0
for student in students:
    if student[2] == 0:
        firstTask = student[0]
    if student[2] == 4:
        print(firstTask, student[0])
        break

