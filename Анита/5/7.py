num = [0] * 6
num = [num[i] + 2 if i % 2 == 0 else num[i] + 1 for i in range(len(num))]
print(num)

num = [str(num[i]) for i in range(len(num))]