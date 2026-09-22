tpl =  tuple() # Creating a tuple with tuple constructor

tpl = ("Blessing", "Roselyn", "Comfort")

tpl1 = ("kate", "Pauline", "Favour")

joined_tpl = tpl + tpl1 # Concatinating two tuples using + operators

family_member = list(joined_tpl) # Converting a tuple into a list to work on it's values

family_member.append("Agnes Odoh") 
family_member.append("Godwin Odoh")

print(joined_tpl)
print(len(joined_tpl))
print(family_member)