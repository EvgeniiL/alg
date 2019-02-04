"""9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""
import random

size = 4
matr = [[0] * size for i in range(size)]

max_min_elem_col = None
min_elem_col = None
min_el = None

for i in range(size):
    for j in range(size):
        matr[i][j] = random.randint(0, 10)
    print(matr[i])

for i in range(size):
    for j in range(size):
        if min_el is None or matr[j][i] < min_el:
            min_el = matr[j][i]
    min_elem_col = min_el
    min_el = None
    if max_min_elem_col is None or min_elem_col > max_min_elem_col:
        max_min_elem_col = min_elem_col

print(max_min_elem_col)
