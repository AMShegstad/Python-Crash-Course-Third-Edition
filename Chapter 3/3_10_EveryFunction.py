"""
Every Function: Think of things you could store in a list. For example, you could make a list of
mountains, rivers, countries, cities, languages, or anything else you'd like. Write a program that
creates a list containing these items and then uses each function introduced in this chapter at 
least once.
"""

programmingLanguages = ['Java', 'Python', 'C++', 'HTML', 'CSS', 'Kotlin', 'JavaScript', 'SQL',  'C#']

# Add a programming language to the list via append()
programmingLanguages.append('Rust')
print(programmingLanguages)

# Add a programming language to the list with insert()
programmingLanguages.insert(3, 'Swift')
print(programmingLanguages)

# Removing an element from the list using del
del programmingLanguages[8]
print(programmingLanguages)

# Removing the last element from the list using pop()
poppedLanguage = programmingLanguages.pop()
print(f"I deleted {poppedLanguage}. I've got enough on my plate already")
print(programmingLanguages)

# Removing Kotlin from the list using pop() and an index
secondPop = programmingLanguages.pop(6)
print(f"I'm still learning, so I'll hold off on {secondPop} for now.")
print(programmingLanguages)

# Removing c# with the remove() method
maybeLater = "C#"
programmingLanguages.remove(maybeLater)
print(programmingLanguages)

# Using sorted() to temporarily sort the list
print(sorted(programmingLanguages))
print(sorted(programmingLanguages, reverse=True))
print(programmingLanguages)

# Using the reverse() method to reverse the order of the list and back again
programmingLanguages.reverse()
print(programmingLanguages)
programmingLanguages.reverse()
print(programmingLanguages)

# Using the sort method to sort the list.
programmingLanguages.sort()
print(programmingLanguages)
programmingLanguages.sort(reverse=True)
print(programmingLanguages)