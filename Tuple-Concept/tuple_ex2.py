fruit = ('banana', 'orange', 'apple')
vegetables = ('carbage', 'carrot')
food_stuff = ('rice', 'beans')

food_stuff_tp = fruit + vegetables + food_stuff
food_stuff_lst = list(food_stuff_tp)
tpl_slice = food_stuff_tp[3:4]
lst_slice1 = food_stuff_tp[:3]
lst_slice2 = food_stuff_tp[0:len(food_stuff_tp)-3]

del food_stuff_tp #Deleting a Tuple 

# Checking if an item is in a Tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Iceland' in nordic_countries:
    print(True)
else:
    print(False)