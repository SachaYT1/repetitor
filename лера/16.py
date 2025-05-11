n = int(input())
speedMax = 0
speedMin = 301
count = 0
for i in range(n):
    speed = int(input())
    if speed >= speedMax:
        speedMax = speed
    if speed <= speedMin:
        speedMin = speed
    if speed <= 30:
        count += 1

print(speedMax - speedMin)
print(count)
