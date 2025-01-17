# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 13:16:18 2022

@author: ander
"""

#Step 1 
import random
from hangman_stages import stages, logo
import hangman_words
word_list = hangman_words.word_list

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

print(logo)

chosen_word = random.choice(word_list)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display=[]
for letter in chosen_word:
    display.append("_")
print(display)


game_completed = False

lives = len(stages)
actual_lives = lives - 1
guess_fail = True

while not game_completed: 
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = str(input("Guess a leter:\n")).lower()
    
    #TODO-2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for pos in range(len(chosen_word)):
        if chosen_word[pos] == guess:
            display[pos] = guess
            guess_fail = False
    
    if guess_fail:
        actual_lives -= 1
        if actual_lives == 0:
            game_completed = True
            print("You fail :(\nThe word is {}".format(chosen_word))
            

    
    
    print(display)
    print(stages[actual_lives])
    guess_fail = True

    # Check if the display is completed
    if display.count("_") == 0:
        game_completed = True
        print("YOU WIN!!!!")
        
        
        
    






















