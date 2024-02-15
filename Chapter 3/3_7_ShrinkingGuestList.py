"""
Shrinking Guest List: You just found out that your new dinner table won't
arrive in time for the dinner, and now you have space for only two guests.

- Start with your program from exercise 3-6. Add a new line that prints a
saying that you can only invite two people for dinner.

- Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you're sorry you can't invite
them to dinner.

- Print a message to each of the two people still on your list, letting 
them know they're still invited.

- Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the
end of your program
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

print("I'm so sorry, but my table won't be here in time and now I can only invite two guests...")

uninvited = names.pop(0)
print(f"I'm so sorry, {uninvited.title()}, but I can no longer invite you to dinner.")
uninvited = names.pop(1)
print(f"I'm so sorry, {uninvited.title()}, but I can no longer invite you to dinner.")
uninvited = names.pop(1)
print(f"I'm so sorry, {uninvited.title()}, but I can no longer invite you to dinner.")
uninvited = names.pop(2)
print(f"I'm so sorry, {uninvited.title()}, but I can no longer invite you to dinner.")
uninvited = names.pop(3)
print(f"I'm so sorry, {uninvited.title()}, but I can no longer invite you to dinner.")
uninvited = names.pop(2)
print(f"I'm so sorry, {uninvited.title()}, but I can no longer invite you to dinner.")

print(names)

print(f"{names[0].title()}, You are still invited to my dinner party. I hope you can make it!")
print(f"{names[1].title()}, you are still invited to my dinner party. I hope you can make it (plus it's at your house...")

del names[0]
del names[0]

print(names)