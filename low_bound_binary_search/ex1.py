def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            right = mid
            