from tasks import task
from tkinter import *

gui = Tk()
gui.geometry('400x300')
gui.title("TO DO List")
taskManager = task()

button_height = 2
button_width = 15

add_button = Button(gui, text="add", fg='black', command=lambda: taskManager.add("hello world"), width=button_width, height=button_height)
add_button.pack(side=TOP, pady=(50, 10))

remove_button = Button(gui, text="remove", fg='black', command=lambda: taskManager.add("hello world"), width=button_width, height=button_height)
remove_button.pack(side=TOP, pady=10)

complete_button = Button(gui, text="mark complete", fg='black', command=lambda: taskManager.add("hello world"), width=button_width, height=button_height)
complete_button.pack(side=TOP, pady=10)

gui.mainloop()

# while True:
#     print("enter what you want to do")
#     print("Press 1 to add")
#     print("Press 2 to remove")
#     print("Press 3 to complete")
#     print("type quit ot quit the program")
#     user_input = input("Enter option: ")

#     if user_input == '1':
#         while True:
#             print("What would you like to add?")
#             string_to_add = input("Enter task: ")
#             bruh = task()
#             bruh.add(string_to_add)
#             bruh.printInfo()
#             print("Enter back to go back")
#             user_input2 = input()
#             if user_input2 == 'back':
#                 break
#     if user_input == '2':
#         print("What would you like to remove")
#     if user_input == '3':
#         print("What would you like to mark complete?")
#     if user_input == 'quit':
#         break