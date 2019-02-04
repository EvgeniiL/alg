"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
arr = [9, 4, 1, 8, 2, 14, 25, 25, 1]
print(arr)
min_el_index = None
max_el_index = None
summ = 0

for i in range(len(arr)):
    if min_el_index is None or arr[i] < arr[min_el_index]:
        min_el_index = i
    if max_el_index is None or arr[i] > arr[max_el_index]:
        max_el_index = i

if max_el_index < min_el_index:
    min_el_index, max_el_index = max_el_index, min_el_index

for i in range(min_el_index + 1, max_el_index):
    summ += arr[i]

print(summ)

