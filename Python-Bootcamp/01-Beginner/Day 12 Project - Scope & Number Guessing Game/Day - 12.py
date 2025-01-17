# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:28:54 2022

@author: ander
"""

# ########################## SCOPE ##########################

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
    
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# # Local Scpoe

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
# drink_potion()
# #print(potion_strength)


# # Global Scpoe

# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#     drink_potion()


# print(player_health)



# # There is no Block Scope

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]
        
#     print(new_enemy)


# # Modifying Global Scope

# enemies = 1

# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
    
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")



# # Global Constants

# PI = 3.141592
# URL = "hhtps://adlsfh"
# TWITTER_HANDLE = "@AngelaYu"

# def calc():
#     print(PI * 2)


# calc()



#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random


def reduce_attempts(attempts):
    return attempts - 1

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100\n")
    dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = 0
    if dificulty == "easy":
        attempts = 10
        print(art.easy_mode)
    elif dificulty == "hard":
        attempts = 5
        print(art.hard_mode)
    else:
        print("Error choosing dificulty!!!!")
    
    pc_number = random.randint(0, 100)
    print(f"The pc number is {pc_number}")
         
    game_done = False
    
    print(f"You have {attempts} attempts remainig to guess the number")
    while not game_done:
        
        guess = int(input("Make a guess: "))
        
        if attempts == 1 and guess != pc_number:
            game_done = True
            print("Game over")
        elif guess > pc_number:
            print("Too High.\nGuess again.")
            attempts = reduce_attempts(attempts)
            print(f"You have {attempts} attempts remainig to guess the number")
        elif guess < pc_number:
            print("Too Low.\nGuess again.")
            attempts = reduce_attempts(attempts)
            print(f"You have {attempts} attempts remainig to guess the number")
        else:
            print(f"You win, the answer was {pc_number}")
            game_done = True
    
game()    
    
    
    
    
    
    
# Forma propuesta
from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Check answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# make funciton to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    print(logo)
    # Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    
    turns = set_difficulty()
    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remainig to guess the number")
    
    
    # Let the user guess a number.
    guess = int(input("make a guess: "))
    
    # Track the number of turns and reduce buy 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
        print("You've run out of guesses, you lose.")
    elif guess != answer:
        print("Guess again.")

game()







































































































































































































































































































