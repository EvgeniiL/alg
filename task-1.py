"""1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9."""
arr = [int(i) for i in range(2, 100)]

numbs = {2, 3, 4, 5, 6, 7, 8, 9}
count = 0

for num in numbs:
    count = (len(arr) + 1) // num
    print(f"{num}: {count}")
    count = 0