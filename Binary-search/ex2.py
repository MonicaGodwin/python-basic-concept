numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11

left = 0
right = len(numbers) - 1
while left <= right:
    mid = (left + right) // 2
    