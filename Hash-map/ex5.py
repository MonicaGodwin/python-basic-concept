numbers = [4, 5, 4, 2, 5, 4, 3, 2]
count = {}
for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

highest_frequency = 0

most_frequent_number = 0

for key, value in count.items():
    if value > highest_frequency:
        highest_frequency = value
        most_frequent_number = key
print(highest_frequency)
print(most_frequent_number)