nums = [1, 2, 2, 2, 2, 5, 7, 9, 9]
target = 1
left = 0
right = len(nums) - 1
answer = -1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        answer = mid
        right = mid - 1
    elif nums[mid] > target:
        right = mid - 1
    elif nums[mid] < target:
        left = mid + 1
print(answer)

