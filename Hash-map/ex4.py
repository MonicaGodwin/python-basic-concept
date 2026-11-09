nums1 = [8, 2, 5, 7, 9, 3]
nums2 = [4, 5, 8, 1, 3, 6]

result = []

num1_con = set(nums1)
for num in nums2:
    if num in num1_con:
        result.append(num)
print(result)
   