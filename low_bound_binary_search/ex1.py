def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            answer = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return answer
result = lower_bound([1,2,2,3,5,6,7], 2)
print(result)