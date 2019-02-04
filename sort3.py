from random import randint, choice

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = choice(arr)
    small = []
    medium = []
    large = []

    for item in arr:
        if item < pivot:
            small.append(item)
        elif item == pivot:
            medium.append(item)
        elif item > pivot:
            large.append(item)
        else:
            print("Что то не так o_O")

    return quick_sort(small) + medium + quick_sort(large)

size = 9
arr = [randint(1, 50) for i in range(size)]
print(arr)
arr = quick_sort(arr)
print(arr)
print(arr[(size - 1) // 2])

