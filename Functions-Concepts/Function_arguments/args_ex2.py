def calculate_average(*numbers):
    num_length = len(numbers)
    total = 0
    for num in numbers:
        total += num
    average = total / num_length
    return average
print(calculate_average(10, 20, 30))
