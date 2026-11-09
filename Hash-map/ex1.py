numbers = [4, 2, 4, 3, 2, 4, 5, 3]
result = {}
for num in numbers:
    if num in result:
        result[num] += 1
    elif num not in result:
        result[num] = 1
print(result)