"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""
rows = 4
cols = 5
matr = [[0] * cols for i in range(rows)]
rows_summ = 0

for i in range(len(matr)):
    for j in range(len(matr[i]) - 1):
        matr[i][j] = int(input("Введите число: "))
        rows_summ += matr[i][j]
    matr[i][len(matr[i]) - 1] = rows_summ
    rows_summ = 0
    print("-------------")

for i in matr:
    print(i)