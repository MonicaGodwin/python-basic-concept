numbers = [10, 20, 30, 40, 10, 20, 50, 30]
seen = set()
for num in numbers:
    if num in seen:
        print(num)
        break
    else:
        seen.add(num)
