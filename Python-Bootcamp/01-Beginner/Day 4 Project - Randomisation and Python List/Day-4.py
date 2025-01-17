# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 21:56:21 2022

@author: ander
"""


import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)


print(my_module.pi)


# 0.00000000 - 0.99999999
random_float = random.random() * 5
print(random_float)



love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")


# day 4-1-exercise
coin = random.randint(0, 1)
if coin == 1:
    print("Heads")
else:
    print("Tails")
    
    
    
    
    
    
# List to store data
state1 = "Delaware"
state2 = "Pennsilvania"
#....

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]

states_of_america[2] = "Jersey nuevo"

states_of_america.append("Append")
states_of_america.extend(["Extend"*2])

print(states_of_america)



# day 4-2-exercise
names = str(input("Who are playing: "))
names = names.split(", ")

lucky = random.randint(0, len(names))

print(names[lucky])




# Separate fruits and vegetables
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches",
               "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]


print(dirty_dozen[1][1])



# Day 4-3 Treasure Map
  
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put the treasure?")

#row = int(int(position) / 10) 
#col = int(int(position) - 10*row)

vertical, horizontal = position[0], position[1]

map[vertical - 1][horizontal - 1] = "X"

"""
if row > 3 or col > 3:
    print("Incorrect position")
elif row == 1:
    row1[col - 1] = "X"
    print(f"{row1}\n{row2}\n{row3}\n")
elif row == 2: 
    row2[col - 1] = "X"
    print(f"{row1}\n{row2}\n{row3}\n")
else: 
    row3[col - 1] = "X"
    print(f"{row1}\n{row2}\n{row3}\n")
"""




# Day 4 - Final project
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
option = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

import random
pc = random.randint(0, 2)

## Pintar los resultados
print(option[player])
print("Computer chose:\n" + option[pc])

if player >= 3 or player < 0: 
  print("You typed an invalid number, you lose!") 
if player == pc:
    print("It's a draw")
elif player == 0 and pc == 2:
    print("You win!!!")
elif player > pc and pc != 0:
    print("You win!!!")
else:
    print("You lose")
    
    












