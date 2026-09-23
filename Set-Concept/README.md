# Set
Set is the collection of unordered and un-indexed distinc elements(i.e elements that are unique, individual and completely different from one another)

# Creating an emppty set

* st = set()

# creating a set with initial items

* st = {'item1', 'item2', 'item3', 'item4'}

# Getting set lenght

* len(st)

# Checking an item

to chech if an item exist in a set, use the "in" membership operator

# Adding items to a set

once set is created, changing an item is not possible, but item or items can be added. 

* using add(): to add just one item the a set

st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')

* using update(): to add multiple items to a set

st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])

# Adding tuple individually  to a list using update()

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)

# Removing items from a set

* use remove() method to remove an item from a set.
* use pop() to remove a random item from a set. It returns the removed item

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()

# Deleting a set

use del to delete the set itself

# Joining sets

sets can be joined using different methods.

* union(): returns a new set

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2

* update(): insert a set into a given set

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1

# findng intersection items

intersection returns a set of items which are in both the sets using & symbol.

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
or using this : st1 & st2

# Checking Subset and Super Set

* subset: set A is a subset of set B if every single item in A is also found in B

** subset: issubset()

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True

* superset: B is the superset of A if B contains every single element that belongs to A.

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

# Finding Symmetric Difference Between Two Sets

It means that it returns a set that contains all items from both sets, except items that are present in both sets.

* using ^ operator

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

result1 = set_a ^ set_b
print(result1)  # Output: {1, 2, 3, 6, 7, 8}


* Using the method .symmetric_difference()

result2 = set_a.symmetric_difference(set_b)
print(result)  # Output: {1, 2, 3, 6, 7, 8}


# Joining Set 2

If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
