def sort_(array1, array2):
    if min(array1) > min(array2):
        array1, array2 = array2, array1
    while len(array2) != 0:
        for j in range(len(array1) - len(array2), len(array1)):
            if array1[j] >= array2[0]:
                array1.insert(j, array2.pop(0))
                break
            if len(array2) == 1:
                array1.append(array2.pop(0))

    return array1

array1 = [1, 6, 5, 10, 25]
array2 = [2, 78, 7, 15, 4, -4]

print(array1)
print(array2)
print("------------------------")
print(sort_(sorted(array1), sorted(array2)))