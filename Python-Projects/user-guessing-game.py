import random


def guess(x):
    random_num = random.randint(1, x)
    guess = 0 # we want our guess to at
    # first try never be equal to random_num
    while guess != random_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        # print(guess)
        if guess < random_num:
            print("Too low! Guess again.")
        elif guess > random_num:
            print("Too high! Guess again.")

    print(f"Yay, congrats! You have guessed the number {random_num} correctly!")


guess(10)