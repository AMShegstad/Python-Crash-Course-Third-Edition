"""
Dinner Guests: Working with one of the programs from Exercises 3-4 to 3-7, use
len() to print a message indicating the number of people you're inviting to 
dinner
"""

names = ["brandon sanderson", "brian hamer jr.", "tiffany shegstad", "gary gygax", "stephen spielberg"]

print(f"Dear, {names[0].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[1].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[2].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[3].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.")
print(f"Dear, {names[4].title()}, the honor of your presence is requested at my humble home for the purpose of an evening of conversation over dinner. Please RSVP.") 

guestCount = len(names)
guestCountMessage = f"\nThere will be {guestCount} guests attending is everyone RSVPs 'Yes'."
print(guestCountMessage)