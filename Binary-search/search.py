numbers = [2, 4, 6, 8, 10, 12, 14, 16]
target = 12
# for num in range(len(numbers)):
#     if numbers[num] == target:
#         print(num)

left = 0
right = len(numbers)-1
while left <= right:
    mid = (left + right) // 2
    if numbers[mid] < target:
        left = mid + 1
    elif numbers[mid] == target:
        print(mid)
        