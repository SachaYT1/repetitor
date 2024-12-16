import itertools

def valid_combination(combination):
    # Проверяем, что A, B, C, D не стоят рядом с нечетными цифрами
    for i in range(1, len(combination) - 1):  # Пропускаем начало и конец строки
        if combination[i] in '13579':
            if combination[i-1] in 'ABCD' or combination[i+1] in 'ABCD':
                return False
    return True

combinations = []
for combination in itertools.product('0123456789*', repeat=5):
    if valid_combination(combination):
        combinations.append(combination)

count = sum(1 for _ in combinations)
print(count)
