arr = [8, 3, 15, 6, 6, 10, 7, 4, 2]
chet_index = []

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        chet_index.append(i)

print(chet_index)