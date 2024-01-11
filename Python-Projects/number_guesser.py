import random

# r = random.randrange(-1, 11) # give us number between 0 to 10
# print(r)
#
# i = random.randint(-1, 11) # give us number between -1 to 11
# print(i)


top_of_range = input("Type a random number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than 0")
        quit()

else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
print(random_number)
attempts = 0

while True:
    attempts += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue  # bring us back to the top


    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Too high")
    else:
        print("Too low")

print(f"You got it in {attempts} attempts")