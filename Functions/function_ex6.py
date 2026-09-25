def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
result = is_even(555)
print(result)

# or

def is_even(num):
   return num % 2 == 0
result = is_even(555)
print(result)

numbers = [2, 5, 8, 11, 14, 4, 10]
def count_even_numbers(nums):
    count = 0
    for num in nums:
        if is_even(num):
            count += 1
    return count
print(count_even_numbers(numbers))


numbers = [2, 5, 8, 11, 14, 10, 4, 7]
def count_odd_num(nums):
    count = 0
    for num in nums:
        if not is_even(num):
            count += 1
    return count
print(count_odd_num(numbers))