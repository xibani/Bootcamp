#
# with open("./Data/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
# with open("./Data/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(row[1])
#     print(temperature)
#
#
# import pandas as pd
# data = pd.read_csv("./Data/weather_data.csv")
# print(data)
# print(data['temp'])
#
#
# temp_list = data['temp'].to_list()
# print(len(temp_list))
#
# print(data['temp'].mean())
# print(data['temp'].max())
#
# # Get data in Columns
# print(data['condition'])
# print(data.condition)
#
# # Get dat in Columns
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp) * 9/5 + 32
# print(monday_temp)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("./Data/new_data.csv")

"""
Crear un dataset con: Fur Color, Count
"""
# import pandas as pd
# data = pd.read_csv("./Data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# squirrel = data['Primary Fur Color'].value_counts()
# print(squirrel)
#
# # squirrel = pd.DataFrame(data=squirrel,
# #                         columns=["Fur Color", "Count"])
# # squirrel.to_csv("./Data/squirrel_count.csv")
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("./Data/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("./Data/states_to_learn.csv")
        break


    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
