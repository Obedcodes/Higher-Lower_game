import art
import game_data
import random
from replit import clear


def format_data(account):
    """Takes the account data and returns it into printable format"""
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}."


def check_answer(guess, a_followers, b_followers):
    """Use if statement to chck if the user is correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Print the logo
print(art.logo)
score = 0
game_should_continue = True
second_person = (random.choice(game_data.data))
# Make the game repeatable
while game_should_continue:
    first_person = second_person
    second_person = (random.choice(game_data.data))
    while first_person == second_person:
        second_person = (random.choice(game_data.data))

    print(f"Compare A: {format_data(first_person)}")
    print(art.vs)

    print(f"Compare B: {format_data(second_person)} ")
    # Ask user for who has more followers
    guess = input("Who has more followers? Type 'A' or 'B' ").lower()
    # Check if user is correct
    a_follower_count = first_person['follower_count']
    b_follower_count = second_person['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # Clear Screen between rounds
    clear()
    print(art.logo)
    # Givefeedback and keep score
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")

    else:
        game_should_continue = False
        print(f"Sorry that's wrong. Final_score: {score}.")


