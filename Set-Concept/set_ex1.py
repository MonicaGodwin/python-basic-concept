# Define the sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Method 1: Using the ^ operator
result1 = set_a ^ set_b

# Method 2: Using the method
result2 = set_a.symmetric_difference(set_b)

print(result2)  # Output: {1, 2, 3, 6, 7, 8}