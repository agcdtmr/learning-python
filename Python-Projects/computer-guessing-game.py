import random


def computer_guess(x):
    print(f"Please choose your secret random number between 1 and {x}")
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be low bc low = high

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly!")


number = 1000

computer_guess(number)

