"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""
this_number = None
count = 0
numbers = int(input("Введите вашу последовательность: "))
number = int(input("Введите цифру: "))

while numbers >= 1:
    this_number = numbers % 10
    if this_number == number:
        count += 1
    numbers //= 10

print(f"цифра {number} встречается в последовательности {count} раз")