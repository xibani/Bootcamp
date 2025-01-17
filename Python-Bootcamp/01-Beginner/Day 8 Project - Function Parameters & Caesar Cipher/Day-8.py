# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 18:01:52 2022

@author: ander
"""

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it in {location}")
    
greet_with(location="yo", name="txiba")



# Day 8.1 - Area Calculation
#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area/cover)
    print(f"The area of the wall is {area}\nand it takes {num_of_cans} cans of paint.")






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# 569875423


#  Day 8.2 - Prime numbers
#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        
    if is_prime:
        print(f"{n} it is a prime number")
    else:
        print(f"{n} it is a prime number")
    

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


















# Caesar Cipher
import art

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
        
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)   
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
            
            
    print(f"The {cipher_direction}d text is {end_text}")
    
    
    
    

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    #Don't change the code above 👆
    
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no" or result == "n":
        should_continue = False
        print("Goodbye")