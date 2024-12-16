def count_pairs_efficient(numbers):
    k21 = k3 = k7 = k = 0

    for num in numbers:
        if num % 3 == 0 and num % 7 == 0:
            k21 += 1
        elif num % 7 == 0:
            k7 += 1
        elif num % 3 == 0:
            k3 += 1
        else:
            k += 1

    countPairs = k3 * k + k3 * (k3 - 1) // 2 + k7 * k + k7 * (k7 - 1) // 2
    return countPairs


def count_pairs_not_efficient(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = numbers[i] * numbers[j]
            if (product % 3 == 0 or product % 7 == 0) and not (product % 3 == 0 and product % 7 == 0):
                count += 1
    return count


f_A = open('27.A.txt').readlines()
f_B = open('27.B.txt').readlines()

numbersA = [int(i) for i in f_A][1:]
numbersB = [int(i) for i in f_B][1:]


print(count_pairs_not_efficient(numbersA))
print(count_pairs_efficient(numbersB))