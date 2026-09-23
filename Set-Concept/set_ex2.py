set_a = {3,7,2,9,1}
set_b = {4,6,5,8,7}

set_c = set_a.union(set_b) # joining two set
print(set_c)

print(set_a.intersection(set_b)) # intersection

print(set_a.issubset(set_b))  # checking subset

print(set_a.isdisjoint(set_b)) # checking for common items

print(set_a.symmetric_difference(set_b))


del set_a
del set_b

print(set_a)











