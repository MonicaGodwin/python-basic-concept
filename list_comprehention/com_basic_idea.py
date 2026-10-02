## LIST COMPREHENSION BASIC IDEA

# result = []

# for num in numbers:
#     if num % 2 == 0:
#         result.append(num)

# print(result)

numbers = [1, 2, 3, 4, 5, 6]


result = [num * num for num in numbers if num % 2 == 0]
print(result)


names = ["Monica", "John", "Alex", "David", "Lucy"]

result = [name for name in names if len(name) > 4]
print(result)

result2 = [name.upper() for name in names if len(name) > 4]
print(result2)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [num * 10 for num in numbers if num % 2 == 1]
print(result)