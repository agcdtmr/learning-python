
# Help me select who to contact


import random

circle = [
    "Daga",
    "Calleja",
    "Herminia Clan",
    "Elem friends",
    "Marga & Princess",
    "Magaganda",
    "Rebecca",
    "JEE",
    "RC Cola",
    "Athina Gracia",
    "Jeremy",
    "Paulo",
    "Charmaine",
    "The Medical City",
    "Telus",
    "The Water District Tanay",
    "Aupair friends in NL",
    "Aupair friends in Brussels",
    "Bilderberg",
    "Taalmaatjes",
    "Taal les kennissen",
    "Yugto acquaintances",
    "LinkedIn Network",
    "100 Devs",
    "Diwata friends",
    "Ateneo LSE",
    "Host a Sister",
    "Girl Gone International"
]

# random.randint(1, 5) --> random number between 1 and 5
# random.choice(array) --> random item in this array

selected = random.choice(circle).upper()

print(f"You should contact {selected} today!\n")