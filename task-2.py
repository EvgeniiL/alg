"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то
у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
ПРИ УСЛОВИИ ИДЕАЛЬНОГО ПОЛЬЗОВАТЕЛЯ!
"""

number = int(input("Введите число: "))
check_number = None

chet_numbers = 0
nechet_numbers = 0

while number >= 1:
    check_number = number % 10
    if check_number % 2 == 0:
        chet_numbers += 1
    else:
        nechet_numbers += 1
    number //= 10

print(f"нечетных: {nechet_numbers}\nчетных: {chet_numbers}")
