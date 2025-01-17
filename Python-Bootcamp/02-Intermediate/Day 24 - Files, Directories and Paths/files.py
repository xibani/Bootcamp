
# # Forma 1 de abrir documentos
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
#
#
# # Segunda forma de abrir documentos
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#
# # w te borra todo y lo sustituye
# with open("my_file.txt", mode="w") as file:
#     file.write("New text para la escribicion")
#
# with open("my_file.txt", mode="a") as file:
#     file.write("\nSegundo New text para la escribicion")


# PATH = "C:/Users/ander/OneDrive/Desktop/"
#
# with open(PATH + "my_file.txt") as file:
#     print(file.read())
#

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/Starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

