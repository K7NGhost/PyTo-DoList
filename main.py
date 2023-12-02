from tasks import task
from tkinter import *

root = Tk()

root.title("TO DO List")
root.geometry('350x350')
root.mainloop()
while True:
    print("enter what you want to do")
    print("Press 1 to add")
    print("Press 2 to remove")
    print("Press 3 to complete")
    print("type quit ot quit the program")
    user_input = input("Enter option: ")

    if user_input == '1':
        while True:
            print("What would you like to add?")
            string_to_add = input("Enter task: ")
            bruh = task()
            bruh.add(string_to_add)
            bruh.printInfo()
            print("Enter back to go back")
            user_input2 = input()
            if user_input2 == 'back':
                break
    if user_input == '2':
        print("What would you like to remove")
    if user_input == '3':
        print("What would you like to mark complete?")
    if user_input == 'quit':
        break