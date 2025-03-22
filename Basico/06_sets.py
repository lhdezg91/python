### Sets ###
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
# Sets are unordered, so you cannot be sure in which order the items will appear.
# no es ordenado, no se puede acceder por indice
# no se puede modificar pero si agregar o eliminar
# no se puede repetir elementos
# no se puede acceder por indice


# Create a set
my_set = set()
my_set = {"apple", "banana", "cherry"} 
print(my_set)

# Access Items
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in my_set:
  print(x)

print("banana" in my_set)   #chequear si existe true o false

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.
my_set.add("orange")
print(my_set)

# Add Sets
# To add items from another set into the current set, use the update() method.
my_set.update(["orange", "mango", "grapes"])
print(my_set)

# Get the Length of a Set
print(len(my_set))

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
my_set.remove("banana")
print(my_set)

# The clear() method empties the set:
my_set.clear()
print(my_set)

# The del keyword will delete the set completely:
del my_set
# print(thisset) # this will raise an error because the set
# is no longer exist

# Join Two Sets
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 

set1.update(set2)
print(set1) 

# The set() Constructor
# It is also possible to use the set() constructor to make a set.

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Set Methods
# Python has a set of built-in methods that you can use on sets.
# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others
#
