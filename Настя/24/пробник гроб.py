def max_sequence_with_ratio(file_path):
    # Считываем содержимое файла
    with open(file_path, 'r') as file:
        data = file.read().strip()

    max_length = 0
    balance_map = {0: -1}  # Словарь для хранения первого появления баланса
    balance = 0

    for i, char in enumerate(data):
        if char in 'KLMN':
            balance += 2  # Буква добавляет 2 к балансу
        elif char in '123':
            balance -= 1  # Цифра вычитает 1 из баланса

        # Если баланс уже встречался, обновляем максимальную длину
        if balance in balance_map:
            max_length = max(max_length, i - balance_map[balance])
        else:
            # Запоминаем первое появление баланса
            balance_map[balance] = i

    return max_length

# Пример использования
file_path = '24.txt'  # Укажите путь к вашему файлу
result = max_sequence_with_ratio(file_path)
print(f"Максимальная длина последовательности: {result}")
