"""
Changing Guest List: You jsut heard that one of your guests cannot make it to 
the dinner, so you need to send out a new set of invivations. You'll have to
think of someone else to invite.

- Start with your program from Exercise 3-4. Add a print() call at the end 
    of your program, stating the name of the guest who cannot make it.

- Modify your list, replacing the name of the guest who cannot make it with
    the name of the new person you are inviting.

- Print a second set of invitation messages, one for each person who is still
    on your list.
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

