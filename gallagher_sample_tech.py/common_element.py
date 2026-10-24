a = [1, 2, 3, 4]
b = [3, 4, 5, 6]


# common = list(set(a) & set(b))
# print(sorted(common))
common = []

for n in a:

    if n in b:
        common.append(n)
print(common)
