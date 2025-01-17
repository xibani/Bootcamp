numbers = [1, 2, 3]
new_number = [n + 1 for n in numbers]
print(new_number)

name = "Ander"
new_name = [letter for letter in name]
print(new_name)

range_list = [2 * n for n in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

"""
Challenges
"""
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [number ** 2 for number in numbers]

# Write your code 👆 above:

print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:

result = [number for number in numbers if number % 2 == 0]

# Write your code 👆 above:

print(result)

with open("./Data/file1.txt") as file1:
    file1_data = file1.readlines()
with open("./Data/file2.txt") as file2:
    file2_data = file2.readlines()

# result = [new_irwm for item in list if test]
result = [int(num) for num in file1_data if num in file2_data]
# Write your code above 👆

print(result)

# Dictionary Comprehesion
print(names)
import random

# students_scores = {new_key:new_value for item in list}
students_scores = {student: random.randint(0, 100) for student in names}
print(students_scores)

# passed_students = {new_key:new_valor for (key, value) in dictionary.items()}
passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
print(sentence.split())
result = {word: int(len(word)) for word in sentence.split()}

print(result)



weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
weather_f = {day: temp*9/5+32 for (day, temp) in weather_c.items()}

# Write your code 👇 below

print(weather_f)






student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)






