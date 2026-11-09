numbers = [7, 3, 5, 7, 2, 3, 9, 5, 1]
empty = set()
for num in numbers:
    if num not in empty:
        empty.add(num)
    else:
        print("duplicate found")
print(empty)