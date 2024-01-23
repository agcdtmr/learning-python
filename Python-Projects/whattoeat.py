
# Help me select what to eat


import random

ulam = [
  "mash potato",
  "bolognese",
  "fritata",
  "sinigang",
  "chicken teriyaki",
  "bulgur",
  "egg + spinach",
  "sopas",
  "dumplings soup",
  "pancake",
  "mantis",
  "yogurt sauce",
  "courgette, carrot, celery soup",
  "aubergine, sambal, tomato",
  "creamy spinach, pasta",
  "sushi burrito",
  "menudo",
  "pansit",
  "chicken, ketchup manis, ketchup asin, oyster sauce"
]

# random.randint(1, 5) --> random number between 1 and 5
# random.choice(array) --> random item in this array

selected = random.choice(ulam).upper()

print(f"You should cook {selected} today!\n")
