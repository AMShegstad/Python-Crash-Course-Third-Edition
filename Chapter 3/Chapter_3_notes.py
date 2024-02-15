# Alexander Shegstad
# Chapter 3 notes and examples

# LISTS
# A list is a collection of items in a particular order. Anything can go into a list, and they don't necessarily need 
# to be related to each other. In Python, square brackets [] indicate a list, and individual elements are to be 
# separated by commas.

ingredients = ["garlic", "salt", "chicken", "tomatoes", "pepper", "lemon", "cream", "pasta"]
print(ingredients)

# Lists are ordered collections, and you can access items in the collection by referring to its index.
print(ingredients[3])

# You can also use the previously learned String methods on the values in the collection
print(ingredients[2].upper())

# Index positions start at 0, and not at 1. The first location is always list[0], so be wary when accessing the correct value.
print(ingredients[0])

# If you want to access the last element in the list, you can simply use -1 as the index
print(ingredients[-1])

# You can use values from a list just as you can variables in things like f-strings as well.
message = f"My lemon-cream chicken with pasta is made with {ingredients[0]}, {ingredients[6]}, and of course, {ingredients[2]}"
print(message)

# The syntax for modifying a list is similar to the syntax for accessing an element. 
cars = ["Ford", "Dodge", "Buick", "Jeep"]
print(cars)

cars[2] = "Nissan"
print(cars)
 
# Adding elements to a list
cars.append("Ferrari")
print(cars)

# You can also use the append() method to fill lists dynamically.
colors = []
colors.append("red")
colors.append("blue")
colors.append("black")
colors.append("yellow")
print(colors)

# Inserting elements into a list can be done with the insert() method. Simply indicate the index for insertion,
# and all elements will be shifted up an index location, starting with the specified index.
colors.insert(2, "violet")
print(colors)

# You can remove elements from a list using the del statement...
del colors[2]
print(colors)

# ..but you can also use the pop() method, which gives the user access to the removed data when removing it from the list.
# Without specifying an index, it will pop the last item in the list, or index -1
popped_color = colors.pop()
print(popped_color)
print(colors)

# It is also possible to give a index to pop specific elements from the list.
index_pop = colors.pop(0)
print(index_pop)
print(colors)

# It is not necessary to use an index to remove data. If you know the value, you can simply refer to it that way.
tech_brands = ["LG", "Sony", "Microsoft", "Philips", "Lenovo", "Apple", "Amazon", "TCL"]
tech_brands.remove('LG')
print(tech_brands)

# You can also use the remove method to work with a value that is being removed from a list.
# This is achieved by giving a variable the same value before performing the removal with said variable.
seemsCheap = "TCL"
tech_brands.remove(seemsCheap)
print(tech_brands)
print(f"\nI just think that {seemsCheap} seems like a cheap and inferior product.")

