nums = [1, 2, 2, 3, 4, 3]

# print(set(nums))

result = []

for n in nums:

    if n not in result:

        result.append(n)

print(result)


