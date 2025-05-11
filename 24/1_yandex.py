f = open('yandex_1.txt')

n = int(f.readline())

requirementPoints = list(map(int, f.readline().split()))
print(requirementPoints)

students = []

for _ in range(n):
    data = list(map(int, f.readline().split()))
    student_id = data[0]
    scores = data[1:]
    
    # Count failed subjects
    failed_count = sum(1 for i in range(4) if scores[i] < requirementPoints[i])
    total_score = sum(scores)
    
    students.append([student_id, scores[0], scores[1], scores[2], scores[3], total_score, failed_count])

students.sort(key=lambda x: (
    0 if x[6] == 0 else 1,  # Graduated students first
    x[6],                   # Then by number of failed subjects
    -x[5],                  # Then by decreasing total score
    x[0]                    # Then by increasing ID
))

last_graduated_id = None
for student in students:
    if student[6] == 0:
        last_graduated_id = student[0]
        
first_all_failed_id = None
for student in students:
    if student[6] == 4:
        first_all_failed_id = student[0]
        break

print(last_graduated_id, first_all_failed_id)
