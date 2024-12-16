def min_length_substring(s, target="LOVE"):
    n = len(s)
    target_len = len(target)
    min_length = float('inf')

    # Указатели для скользящего окна
    start = 0
    current_target_index = 0

    for end in range(n):
        # Если текущий символ совпадает с нужным символом из "LOVE"
        if s[end] == target[current_target_index]:
            current_target_index += 1

            # Если найдено полное слово "LOVE"
            if current_target_index == target_len:
                # Сжимаем окно, пока это возможно
                while current_target_index == target_len:
                    if s[start] == target[0]:
                        current_target_index -= 1
                    start += 1

                # Обновляем минимальную длину
                min_length = min(min_length, end - start + 2)

    return min_length if min_length != float('inf') else -1


# Чтение строки из файла
with open("24_18284.txt", "r") as file:
    text = file.read().strip()

# Запуск программы
result = min_length_substring(text)
print(result)
