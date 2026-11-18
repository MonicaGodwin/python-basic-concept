def isBadVersion(version):
    return version >= 1

n = 8

left = 1
right = n
result = 0
while left <= right:
    mid = (left + right) // 2
    if isBadVersion(mid):
        result = mid
        right = mid - 1
    elif isBadVersion(mid) == False:
        left = mid + 1
print(result)