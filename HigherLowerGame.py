from art import logo, vs
from game_data import data
import random


def gen_compare():
    key = random.randint(0, 49)
    return data[key]


def play_game():
    still_play = True
    new_comparison = gen_compare()
    new_comparison2 = gen_compare()
    correct_guesses = 0

    while still_play:

        while new_comparison2 == new_comparison:
            new_comparison2 = gen_compare()

        print(logo)

        print(
            f"Compare A: {new_comparison['name']}, a {new_comparison['description']}, from {new_comparison['country']}.")

        print(vs)

        print(
            f"Compare B: {new_comparison2['name']}, a {new_comparison2['description']}, from {new_comparison2['country']}.")

        user_guess = input("Who has more followers? A or B? Type in your answer: ").upper()

        if new_comparison["follower_count"] > new_comparison2["follower_count"] and user_guess == "A":
            correct_guesses += 1
            print(f"Correct! A Current score: {correct_guesses}")
            new_comparison2 = gen_compare()

        elif new_comparison["follower_count"] < new_comparison2["follower_count"] and user_guess == "B":
            correct_guesses += 1
            print(f"Correct! B Current score: {correct_guesses}.")
            new_comparison = new_comparison2
            new_comparison2 = gen_compare()

        else:
            print(f"Wrong, it's not {user_guess}, so you lose! ")
            print(f"You finished the game with the score of {correct_guesses}")
            still_play = False


play_game()

play_again = input("Do you want to play again? Type 'y' or 'n': ")

if play_again == "y":
    play_game()

