""" 
You just found a bigger dinner table, so now more space is available. Think of
three more guests to invite to dinner.

- Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
    end of your program, informing people that you found a bigger table.

- Use insert() to add one new guest to the beginning of your list.
- Use insert() to add one new guest to the middle of your list.
- Use append() to add one new guest to the end of your list.
- Print a new set of invitations, one for each person who is still in your list.
"""

names = ["brandon sanderson", "brian hamer jr.", "tiffany shegstad", "gary gygax", "stephen spielberg"]

print(f"Dear, {names[0].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[1].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[2].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[3].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[4].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.") 

print(f"\nOh No! {names[3].title()} is unable to attend!\n")

names[3] = "jade raymond"

print(names)

print(f"Dear, {names[0].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[1].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[2].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[3].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[4].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.") 

print("\nGuess what, guys! I found a larger table so I can invite three more people!\n")

names.insert(0, "John Oliver")
names.insert(2,"Stephen Colbert")
names.append("Pat McAfee")

print(names)

print(f"Dear, {names[0].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[1].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[2].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[3].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[4].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[5].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[6].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[7].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.") 
