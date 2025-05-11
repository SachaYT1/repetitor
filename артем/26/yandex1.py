f = open('yandex_1.txt')
n = int(f.readline())

reqPoints = list(map(int, f.readline().split()))

students = []
for i in range(n):
    student = list(map(int, f.readline().split()))
    id = student[0]
    countZaval = 0
    summaPoints = 0
    for j in range(1, len(student)):
        summaPoints += student[j]
        if student[j] < reqPoints[j - 1]:
            countZaval += 1

    students.append([id, summaPoints, countZaval])


students.sort(
    key = lambda x: (
        x[2],
        -x[1],
        x[0]
    )
)


task1 = 0
task2 = 0
for student in students:
    if student[-1] == 0:
        task1 = student[0]
    elif student[-1] == 4:
        task2 = student[0]
        break
    
    
print(task1, task2)


