import random
import time

"""Сортировка пузырьком по убыванию"""
def bubble_sort_desc(arr):
    """Сортирует массив по убыванию с помощью пузырьковой сортировки."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Обмен элементов для сортировки по убыванию
    return arr

"""Сортировка выбором по убыванию"""
def selection_sort_desc(arr):
    """Сортирует массив по убыванию с помощью сортировки выбором."""
    n = len(arr)
    for i in range(n):
        max_index = i  # Предполагаем, что текущий элемент максимальный
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j  # Находим индекс максимального элемента
        arr[i], arr[max_index] = arr[max_index], arr[i]  # Меняем местами
    return arr

# Создаем массив из 1,000,000 случайных элементов
arr_size = 1_000_0
arr = [random.randint(1, 1_000_0) for _ in range(arr_size)]

# Копируем массив для обеих сортировок
arr_bubble = arr[:]
arr_selection = arr[:]

# Замер времени для пузырьковой сортировки
start_time = time.time()
bubble_sort_desc(arr_bubble)
bubble_time = time.time() - start_time

# Замер времени для сортировки выбором
start_time = time.time()
selection_sort_desc(arr_selection)
selection_time = time.time() - start_time

# Вывод времени выполнения
print(f"Время выполнения пузырьковой сортировки: {bubble_time:.2f} секунд")
print(f"Время выполнения сортировки выбором: {selection_time:.2f} секунд")