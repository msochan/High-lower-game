import random

import art
from game_data import data
import os


def compare():
    if compare_a['follower_count'] > compare_b['follower_count']:
        return 'a'
    else:
        return 'b'


def check_player_answer(player_answer):
    global score
    global is_continue
    global compare_a
    global compare_b
    right_answer = compare()
    if player_answer == right_answer:
        score += 1
        os.system("clear")
        compare_a = compare_b
        while compare_b == compare_a:
            next_compare = random.sample(data, 1)
            compare_b = next_compare[0]
    else:
        is_continue = False
        os.system("clear")
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")


def game_loop():
    while is_continue:
        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
        print(art.vs)
        print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
        choose = (input("Who has more followers? Type 'A' or 'B': ")).lower()
        check_player_answer(choose)


if __name__ == '__main__':
    is_continue = True
    comparison = random.sample(data, 2)
    compare_a = comparison[0]
    compare_b = comparison[1]
    score = 0
    game_loop()
