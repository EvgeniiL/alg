arr = [1, 2, 6, 14, -10, -3, 4, -3, 90]

min_el = None

for i in arr:
    if i < 0:
        if min_el is None or i > min_el:
            min_el = i

print(min_el)