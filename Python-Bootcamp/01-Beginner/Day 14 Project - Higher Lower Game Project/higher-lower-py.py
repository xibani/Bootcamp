# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:38:17 2022

@author: ander
"""

import art
import game_data
import random

from IPython import get_ipython

game_data = game_data.data

def clear_console():
    #get_ipython().magic('clear')
    print("\033[H\033[J")


def random_choice(game_data):
    compare_A = random.choice(game_data)
    compare_B = random.choice(game_data)
    while compare_A == compare_B:
        compare_B = random.choice(game_data)
    
    return compare_A, compare_B


def check_answer(guess, compare_A, compare_B, score):
    continue_playing = False
    if compare_A == compare_B:
        continue_playing = True
        score += 1
    elif compare_A > compare_B and guess == "A":
        continue_playing = True
        score += 1
    elif compare_A < compare_B and guess == "B":
        continue_playing = True
        score += 1
    else:
        score = score
    return score, continue_playing
        


def plot_board(compare_A, compare_B, score):
    clear_console()
    print(art.logo)
    if score != 0:
        print(f"You are right! Current score: {score}")
    print(f"Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}")
    print(art.vs)
    print(f"Against B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}")
    guess = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    while guess != "A" and guess != "B":
        guess = input("Error!!!! Type 'A' or 'B': ").capitalize()
    return guess

def game():
    score = 0
    continue_playing = True
    
    # Get the participants
    while continue_playing:
        compare_A, compare_B = random_choice(game_data)
        guess = plot_board(compare_A, compare_B, score)
        score, continue_playing = check_answer(guess, compare_A["follower_count"], compare_B["follower_count"], score)
        
        if not continue_playing:
            clear_console()
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            
            
game()          
            