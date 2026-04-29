strings = ["Hello bhai\n", "Kaise ho?\n", "Ye second method hai\n"]

with open("multi.txt", "w") as file:
    file.writelines(strings)