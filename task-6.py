"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное
пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random

number = random.randrange(0, 100)
for i in range(9, -1, -1):
    user_number = int(input("Введите число: "))
    if user_number == number:
        print("Поздравляю! Вы угадали!")
        quit()
    elif user_number < number:
        print(f"Число {user_number} меньше загаданного\nОсталось {i} попыток")
    else:
        print(f"Число {user_number} больше загаданного\nОсталось {i} попыток")

print(f"Вы прогирали. Загаданное число: {number}")