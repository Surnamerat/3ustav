import re

def process_command(command, array):

    # Проверки на формат команды
    if not isinstance(command, str):
        raise ValueError("Команда должна быть строкой.")
    if not isinstance(array, list):
        raise ValueError("Второй аргумент должен быть массивом.")

    # Команда: Получить элемент по n индексу
    match_index = re.match(r"Получить элемент по (\d+) индексу", command)
    if match_index:
        n = int(match_index.group(1))
        if 0 <= n < len(array):
            return array[n]
        else:
            raise IndexError(f"Индекс {n} выходит за пределы массива.")

    # Команда: Получить элементы с n по b с шагом v
    match_slice = re.match(r"Получить элементы с (\d+) по (\d+) с шагом (\d+)", command)
    if match_slice:
        n, b, v = map(int, match_slice.groups())
        if n < 0 or b > len(array) or v <= 0:
            raise ValueError("Недопустимые значения для диапазона или шага.")
        return array[n:b:v]

    # Команда: Получить n-ый элемент с конца массива
    match_reverse = re.match(r"Получить (\d+)-ый элемент с конца массива", command)
    if match_reverse:
        n = int(match_reverse.group(1))
        if 1 <= n <= len(array):
            return array[-n]
        else:
            raise IndexError(f"Индекс {n} выходит за пределы массива.")

    # Если команда не соответствует ни одному шаблону
    raise ValueError("Команда не соответствует ни одному допустимому формату.")


# Примеры вызова функции
some_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Пример 1
print(process_command("Получить элемент по 2 индексу", some_array))  # Вывод: 3

# Пример 2
print(process_command("Получить элементы с 1 по 5 с шагом 2", some_array))  # Вывод: [2, 4]

# Пример 3
print(process_command("Получить 3-ый элемент с конца массива", some_array))  # Вывод: 8