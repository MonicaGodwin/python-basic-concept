def isBadVersion(version):
    return version >=6

n = 10
first_bad = 6
left = 1
right = n
result = 0
while left <= right:
    mid = (left + right) // 2
    if isBadVersion(mid) == True:
        result = mid
        right = mid - 1
    elif isBadVersion(mid) == False:
        left = mid + 1
print(result)