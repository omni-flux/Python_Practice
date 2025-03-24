try:
    print("______________________________Welcome to MadLib______________________________")
    name :str  = input("Enter a name:")
    gender :str  = input("Enter a gender 'M' or 'F':").upper()
    while gender not in ['M', 'F']:
        print(f"{gender.lower()} is not a valid gender 🗿, might as well be an attack helicopter 🚁")
        gender = input("Enter a valid gender 'M' or 'F': ").upper()
    pronoun:str = 'he' if gender == 'M' else 'She'
    gender = 'Male' if gender == 'M' else 'Female'
    hobby:str = input("Enter a hobby:")
    verb_a : str = input("Enter a verb:" )
    verb_b:str =input("Enter another verb:")
    place:str =input("Enter a place:")
    while True:
        try:
            age: int = int(input("Enter your age:"))
            break
        except ValueError:
            print("please enter a valid int value")

    print("That's it, That's it... 😓")
    conformation:str =input("are you ready to hear a story y/n:").lower()
    while True:
        if conformation == 'y':
            story:str=f"""
_________________________________________________________________________________________________________________dscnsbd            
            
Once upon a time, there was a {age}-year-old {gender} named {name} who was obsessed with {hobby}. 🎨🚀🕺  
Every single day, {pronoun} would {verb_a} through the {place} like a majestic chicken on roller skates. 🐔🛼  
People stared. Dogs barked. Even the pigeons were confused. 🐦💬 "Is this performance art?"\n  
One day, while dramatically trying to {verb_b} like a professional, {name} accidentally crashed into a food cart. 
BOOM! 🌭🍔🍕 Ketchup rained from the heavens. A dramatic slow-motion gasp filled the air. 
"NOOO!" screamed the vendor, clutching a half-eaten corn dog. 🌽\n  
But instead of running away, {name} struck a heroic pose. ✨ 
"Fear not! I am the legendary {hobby} champion of {place}!" {pronoun} declared, still dripping in mustard.  
The tourists applauded wildly, thinking this was all part of an immersive street performance. 🎭👏\n  
"Bravo! Art is so unpredictable!" 
And from that day forward, {name} was known as The Ketchup King/Queen/Monarch of {place},  
celebrated for {pronoun}’s dedication to both {hobby} and spontaneous condiment disasters. 🌟🍅👑\n  
The end! 😂   

_________________________________________________________________________________________________________________                     
"""
            print(story)
            break
        elif conformation == 'n':
            print(f"Well suit yourself, {name}. You did all that for nothing 🙄")
            break
        else:
            print("please enter valid confimation 'y' or 'n'")


except Exception as e :
    print(f"Something went wrong😵‍💫, maybe {e}")
except KeyboardInterrupt :
    print(f"Bye Bye, 😒{name}.\n{hobby}is a stupid hobby anyways😏") # i know this will give a un decleared error if the user exits befole entering name or hobby




