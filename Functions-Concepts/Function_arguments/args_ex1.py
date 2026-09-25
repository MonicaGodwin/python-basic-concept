def calculate_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(calculate_numbers(10,20,30, 20, 10,5))