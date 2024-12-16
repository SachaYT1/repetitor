for x in range(0, 17):
    alphabet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G"]
    num1 = int(f'5432{alphabet[x]}67', 17)
    num2 = int(f"302{alphabet[x]}", 17)
    if (num1 + num2) % 19 == 0:
        print(num1 + num2)
