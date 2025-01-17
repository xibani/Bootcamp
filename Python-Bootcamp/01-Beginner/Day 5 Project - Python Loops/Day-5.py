# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 19:13:45 2022

@author: ander
"""



#♣ Day 5.1 - Average Height

student_heights = [156, 178, 165, 171, 187]

average_height = 0.0

for student in student_heights:
    average_height += student
    
average_height /= len(student_heights)
    
print(f"Average is {average_height}")
    


# Day 5.2 - Highest Score

student_scores = input("Input a list of student scores ").split(", ")
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
    
print(max(student_scores))    
    
higest_score = 0
for score in student_scores:
    if score >= higest_score:
        higest_score = score

print(f"The higest score is {higest_score}")



# Day 5.3 - Adding Evens
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)



# Day 5.4 - FizzBuzz

for i in range(1, 101, 1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)











# Day 5 - Random Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# count_leter, count_symbol, count_number = 0, 0, 0
# count_length = nr_letters + nr_symbols + nr_numbers

# password = ""

# c = 0

# while c < count_length:
#     # Generate random value
#     character = random.randint(0, 2)
#     if character == 0 and count_leter < nr_letters: #Add letter
#         password += (letters[random.randint(0, len(letters)-1)])
#         count_leter += 1
#         c += 1
#     elif character == 1 and count_symbol < nr_symbols: #Add symbol
#         password += (symbols[random.randint(0, len(symbols)-1)])
#         count_symbol += 1
#         c += 1
#     elif character == 2 and count_number < nr_numbers: #Add number
#         password += (numbers[random.randint(0, len(numbers)-1)])
#         count_number += 1
#         c += 1
#     else:
#         c = c

# print(str(password))


# # Eazy level
# password = ""

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)



# Hard Level
password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)


password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")


