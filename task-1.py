arr = [int(i) for i in range(2, 100)]

numbs = {2, 3, 4, 5, 6, 7, 8, 9}
count = 0

for num in numbs:
    count = (len(arr) + 1) // num
    print(f"{num}: {count}")
    count = 0