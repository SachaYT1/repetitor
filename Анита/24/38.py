f = open('k7c-6.txt').readline()
count_triples_solution1 = 0
count_triples_solution2 = 0
for i in range(len(f) - 2):
    if f[i] != f[i + 1] and f[i] != f[i + 2] and f[i + 1] != f[i + 2]:
        count_triples_solution1 += 1

    if len({f[i], f[i + 1], f[i + 2]}) == 3:
        count_triples_solution2 += 1

print(count_triples_solution1)
print(count_triples_solution2)
