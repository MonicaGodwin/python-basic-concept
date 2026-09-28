double = lambda number: number * 2
numbers = [1, 2, 3, 4, 5]
mapped = map(double, numbers)
lst = list(mapped)
print(lst)

is_even = lambda number: number % 2 == 0
print(is_even(10))
print(is_even(7))

