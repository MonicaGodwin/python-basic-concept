double = lambda number: number * 2
numbers = [1, 2, 3, 4, 5]
mapped = map(double, numbers)
lst = list(mapped)
print(lst)

is_even = lambda number: number % 2 == 0
print(is_even(10))
print(is_even(7))

numbers = [2, 4, 6, 8]
result = list(map(lambda number: number + 5, numbers))
print(result)