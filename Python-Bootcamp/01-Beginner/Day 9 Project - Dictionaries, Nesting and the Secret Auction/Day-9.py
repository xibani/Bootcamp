# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 10:36:17 2022

@author: ander
"""

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."
                          }

# Retrieving items from dictionary.
print(programming_dictionary["Bug"])


# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)


# Create an empty dicionary
empty_dictionary = {}

# Wipe an exsisting dictioneary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an tiem in dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])


# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    
    
    


# Day 931 - Exercise

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score >= 91:
        grade = "Outstanding"
    elif score >= 81:
        grade = "Exceeds Expectations"
    elif score >= 71:
        grade = "Acceptable"
    elif score <= 70:
        grade = "Fail"
    
    student_grades[student] = grade

    

# 🚨 Don't change the code below 👇
print(student_grades)












# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    }

# Nesting a List in a Dictionary
travel_log ={
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
    }


# Nesting Dictionary in a Dictionary

travel_log ={
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
    }


# Nesting Dictionary in a List
travel_log = [
    {
      "country": "France", 
      "cities_visited": ["Paris", "Lille", "Dijon"], 
      "total_visits": 12
    },
    {
      "country": "Germany", 
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
      "total_visits": 5
    },
]




# Day 9.2 - Dictionary in List

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country_visited, time_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = time_visited
    new_country["cities"] = cities_visited
    
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)







# Blind Auction
from spyder import clear
import art
print(art.logo)

print("Welcome to the secret auction program.\n")

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder] 
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = float(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()
        
























































