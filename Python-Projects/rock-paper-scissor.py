import random


def user_rock_paper_scissor():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer_choice = random.choice(['r', 'p', 's'])

    if user == computer_choice:
        return "It's a tie"

    # r > s, s > p, p > r
    if who_won(user, computer_choice):
        return 'You won!'

        # if who_won(computer_choice, user):
        # who_won(computer_choice, user)
    return 'You lost!'


def who_won(player, opponent):
    # return true if the player wins
    # r > s, s > p, p > r

    if (player == 'r' and opponent == 's') \
            or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True



print(user_rock_paper_scissor())