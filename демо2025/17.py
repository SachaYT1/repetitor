f = open('demo_2025_17.txt').readlines()
a = []
for num in f:
    a.append(int(num))
min_elem = min(a)
count_pairs = 0
max_sum = 0
for i in range(len(a) - 1):
    num1 = a[i]
    num2 = a[i + 1]
    if num1 % 16 == min_elem or num2 % 16 == min_elem:
        count_pairs += 1
        max_sum = max(max_sum, num1 + num2)
print(count_pairs, max_sum)