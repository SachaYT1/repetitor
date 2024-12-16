f = open('24_18284.txt').read()
target = 'LOVE'

n = len(f)
m = len(target)
min_length = 10 ** 10
target_index = 0
start = 0

for end in range(n):
    if f[end] == target[target_index]:
        target_index += 1

        if target_index == m:  # Найдено слово LOVE
            # Сдвигаем указатель start к минимальной подходящей подстроке
            while target_index == m:
                if f[start] == target[0]:
                    target_index -= 1
                start += 1

            min_length = min(min_length, end - start + 2)  # Обновляем минимальную длину

print(min_length)  # Вывод: 7
