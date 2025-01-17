# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 12:57:15 2022

@author: ander
"""

# Functions with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didm't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f"{formated_f_name} {formated_l_name}"
    
print(format_name(input("What is your first name? "), input("What is your last name? ")))






# Day 10-1 exercise

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        is_a_leap_year = True
      else:
        is_a_leap_year = False
    else:
      is_a_leap_year = True
  else:
    is_a_leap_year = False
  return is_a_leap_year

def days_in_month(year, month):
    """Take a fist an last name and format it to return the title case version of the name"""
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    is_a_leap_year = is_leap(year)
      
    if is_a_leap_year == True and month == 2:
        return 29 
    return month_days[month - 1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)









# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Substract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

import art


def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    
    while should_continue:
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculaion. ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()


























