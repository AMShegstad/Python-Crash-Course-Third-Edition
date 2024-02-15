# Alexander Shegstad

# the title() method capitalizes the first letter of every word in the string:
team = "tampa bay buccaneers"
print(team.title())

# the upper() method makes every letter uppercase.
# the lower() method makes every letter lowercase.
actor = "Tom Cruise"
print(actor.upper())
print(actor.lower())

# Sometimes you will want to use variables in strings. To do so, insert an 'f' 
# immediately before the opening quotation mark. Put braces around the name or
# names of any variable you want to use inside the string. Python will replace
# each with the proper value.
game = "grand theft auto"
name = "tiffany"
message = f"{name.title()}'s favorite video game is {game.title()}"
print(message)

# To add a tab/indentation to your text, use the character combination \t
message = "tab\ttab\ttab"
print(message)

# To add a new line in a string, use the character combination \n
message = "each\nword\nis\non\na\nnew\nline\n"
print(message)

# Tabs and New Lines can be added into the same String

# rstrip and lstrip can be used to remove white space from the right and left of the string, respectively.
text1 = "    text    "
text1 = text1.rstrip()
text2 = "    text    "
text2 = text2.lstrip()
print(text1)
print(text2)
# the strip() method removes whitespace from both sides.

# When working with URLs, we can remove particular prefixes with the removeprefix() method. for example:
url = "https://www.AlexanderShegstad.com/"
print(url.removeprefix('https://'))

# You can add, subtract, divide, and multiply integers in Python
addition = 10 + 1
print(addition)

subtraction = 10 - 1
print(subtraction)

division = 100 / 20
print(division)

multiplication = 4 * 3
print(multiplication)

# Exponents can be represented with the use of two asterisks, **
exponent = 4**3
print(exponent)

# Python supports the order of operations. 
orderOfOperations = 2 + 3 * 4 ** 2
print(orderOfOperations)

# Floats in Python with usually work without you having to worry about decimal places and the like.
float = 31.5 + 8.500
print(float)

# Dividing any two numbers will result in a float, always, even if the result is a whole number
floatquotient = 10 / 5
print(floatquotient)

# Additionally, mixing a float and an integer in any other operation will always give you a float
floattest = 33.333 * 3
print(floattest)

# When writing long numbers, you can group digits using underscores to make large numbers more readable
moneyIDontHave = 9_000_000_000
print(moneyIDontHave)

# You can assign values to multiple variables at once using just a single line of code. This can 
# help shorten programs and make them easier to read.
book1, book2, book3, book4, book5 = "The Way Of Kings", "Words Of Radiance", "Oathbringer", "Rythym Of War", "Wind and Truth"
print(book1)
print(book2)
print(book3)
print(book4)
print(book5)

# Constants are variables whose value does not change throughout the entire program. Python does not contain 
# dedicated constant types, but writing the variable's name in ALL_CAPS means it should be treated as 
# constant

