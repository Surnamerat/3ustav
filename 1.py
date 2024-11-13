def max_if_a_positive(b, c):

    a = int(input("Введите число a: "))
    if a > 0:
        return max(a, b, c)
    else:
        return -1

result = max_if_a_positive(3, 5)

print("Результат:", result)