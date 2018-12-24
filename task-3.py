"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
"""

number = int(input("Введите число: "))
reverse_number = ""

while number >= 1:
    reverse_number += str(number % 10)
    number //= 10

print(reverse_number)