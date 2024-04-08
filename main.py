import random
from game_data import data


def get_random_account():
    return random.choice(data)


def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'A'
    else:
        return guess == 'B'


def game():
    start_game = True
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()
    while start_game:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(f"Against B: {format_data(account_b)}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            start_game = False
            print(f"Sorry, that's wrong. Final score: {score}.")


game()
