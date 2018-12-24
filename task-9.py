"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр, если пользователь вводит 0, программа завершается.
"""

user_number = None
number = None
summ_number = 0
max_summ = None
max_summ_number = None

while True:
    user_number = int(input("Введите число: "))
    if user_number == 0:
        break
    else:
        number = user_number
        while user_number >= 1:
            summ_number += user_number % 10
            user_number //= 10
        if max_summ == None or summ_number > max_summ:
            max_summ = summ_number
            max_summ_number = number
        summ_number = 0

print(f"Максимальная сумма цифр у числа {max_summ_number}: {max_summ}")
