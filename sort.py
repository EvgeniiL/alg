from random import randint

def sort_(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr) - 1, 0, -1):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

size = 10

array = [randint(-100, 100) for i in range(size)]
print(array)
print(sort_(array))