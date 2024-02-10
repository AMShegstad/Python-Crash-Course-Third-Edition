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
