import timeit
import random

# Генерація випадкових списків чисел
small_list = [random.randint(0, 1000) for _ in range(100)]
medium_list = [random.randint(0, 1000) for _ in range(1000)]
large_list = [random.randint(0, 1000) for _ in range(10000)]

# Сортування за допомогою алгоритму злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Вимірюємо час сортування на різних наборах даних для різних алгоритмів
merge_sort_small_time = timeit.timeit(lambda: merge_sort(small_list.copy()), number=1)
merge_sort_medium_time = timeit.timeit(lambda: merge_sort(medium_list.copy()), number=1)
merge_sort_large_time = timeit.timeit(lambda: merge_sort(large_list.copy()), number=1)

insertion_sort_small_time = timeit.timeit(lambda: insertion_sort(small_list.copy()), number=1)
insertion_sort_medium_time = timeit.timeit(lambda: insertion_sort(medium_list.copy()), number=1)
insertion_sort_large_time = timeit.timeit(lambda: insertion_sort(large_list.copy()), number=1)

sorted_small_time = timeit.timeit(lambda: sorted(small_list.copy()), number=1)
sorted_medium_time = timeit.timeit(lambda: sorted(medium_list.copy()), number=1)
sorted_large_time = timeit.timeit(lambda: sorted(large_list.copy()), number=1)

# Друк результатів
print("Merge Sort:")
print("Small List Time:", merge_sort_small_time)
print("Medium List Time:", merge_sort_medium_time)
print("Large List Time:", merge_sort_large_time)
print("\nInsertion Sort:")
print("Small List Time:", insertion_sort_small_time)
print("Medium List Time:", insertion_sort_medium_time)
print("Large List Time:", insertion_sort_large_time)
print("\nTimsort:")
print("Small List Time:", sorted_small_time)
print("Medium List Time:", sorted_medium_time)
print("Large List Time:", sorted_large_time)
