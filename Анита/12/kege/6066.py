from itertools import permutations, product
ans = set()
count = 0
for i in permutations('1' * 4 + '3' * 3 + '2' * 2):
    s = "".join(i)
    count += 1

    while '133' in s or '221' in s or '23' in s:
        s = s.replace('133', '1', 1)
        s = s.replace('221', '31', 1)
        s = s.replace('23', '21', 1)

    ans.add(s)
print(count)
print(len(ans))