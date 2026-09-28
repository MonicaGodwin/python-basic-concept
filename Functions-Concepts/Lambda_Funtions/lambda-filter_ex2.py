is_even = lambda number: number % 2 == 0
numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(is_even, numbers))
print(result)

numbers = [10, 15, 20, 25, 30, 35, 40]
result = list(filter(lambda number: number > 20, numbers))
print(result)