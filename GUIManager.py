from tkinter import *
from tasks import task
import subprocess
import threading

someTask = task()
someTask.printInfo

class GUIManagers:
    #creates the first instance of the gui
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x300")
        self.selected_priority = None

        #creating the main frame
        self.main_frame = Frame(root)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.button_width = 15
        self.button_height = 2

        #Adding the buttons
        add_button = Button(self.main_frame, text="add", fg='black', command=self.show_alternate_screen, width=self.button_width, height=self.button_height)
        add_button.pack(side=TOP, pady=(50, 10))

        remove_button = Button(self.main_frame, text="remove", fg='black', command=self.remove_screen, width=self.button_width, height=self.button_height)
        remove_button.pack(side=TOP, pady=10)

        complete_button = Button(self.main_frame, text="mark complete", fg='black', command=self.complete_screen, width=self.button_width, height=self.button_height)
        complete_button.pack(side=TOP, pady=10)

        clear_button = Button(self.main_frame, text="clear tasks", fg='black', command=self.clear, width=self.button_width, height=self.button_height)
        clear_button.pack(side=TOP, pady=10)

    #Shows the add frame in the GUI
    def show_alternate_screen(self):
        self.main_frame.destroy()
        alternate_frame = Frame(self.root)
        alternate_frame.pack(fill=BOTH, expand=True)

        label = Label(alternate_frame, text="Enter task:")
        label.pack(pady=20)

        self.task_entry = Entry(alternate_frame, width=30)
        self.task_entry.pack(pady=10)

        save_button = Button(alternate_frame, text="Save", command=self.save_task)
        save_button.pack(pady=10)
        back_button = Button(alternate_frame, text="Back", command=self.show_main_screen)
        back_button.pack(pady=10)

        button_frame = Frame(alternate_frame)  # Create a new frame for the buttons
        button_frame.pack(side=TOP, pady=10)

        self.low_button = Button(button_frame, text="Low Priority", command=lambda: self.set_priority("Low"))
        self.low_button.pack(side=LEFT, padx=10)
        self.medium_button = Button(button_frame, text="Medium Priority", command=lambda: self.set_priority("Medium"))
        self.medium_button.pack(side=LEFT, padx=10)
        self.high_button = Button(button_frame, text="High Priority", command=lambda: self.set_priority("High"))
        self.high_button.pack(side=LEFT, padx=10)


        #something to reference in the show_main_screen
        self.alternate_frame = alternate_frame

    #Switches to the remove frame
    def remove_screen(self):
        self.main_frame.destroy()
        remove_frame = Frame(self.root)
        remove_frame.pack(fill=BOTH, expand=True)

        label = Label(remove_frame, text="Enter index of task to remove")
        label.pack(pady=20)

        self.index_entry = Entry(remove_frame, width=10)
        self.index_entry.pack(pady=10)

        save_button = Button(remove_frame, text="Save", command=self.save_index)
        save_button.pack(pady=10)
        back_button = Button(remove_frame, text="Back", command=self.show_main_screen)
        back_button.pack(pady=10)

    def complete_screen(self):
        self.main_frame.destroy()
        complete_frame = Frame(self.root)
        complete_frame.pack(fill=BOTH, expand=True)

        label = Label(complete_frame, text="Enter index of task to mark done")
        label.pack(pady=20)

        self.index_entry = Entry(complete_frame, width=10)
        self.index_entry.pack(pady=10)

        save_button = Button(complete_frame, text="Save", command=self.complete_index)
        save_button.pack(pady=10)
        back_button = Button(complete_frame, text="Back", command=self.show_main_screen)
        back_button.pack(pady=10)

    def show_main_screen(self):
        self.clear_all_frames()
        self.root.geometry("400x300")
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True)

        add_button = Button(self.main_frame, text="add", fg='black', command=self.show_alternate_screen, width=self.button_width, height=self.button_height)
        add_button.pack(side=TOP, pady=(50, 10))
        remove_button = Button(self.main_frame, text="remove", fg='black', command=self.remove_screen, width=self.button_width, height=self.button_height)
        remove_button.pack(side=TOP, pady=10)
        complete_button = Button(self.main_frame, text="mark complete", fg='black', command=self.complete_screen, width=self.button_width, height=self.button_height)
        complete_button.pack(side=TOP, pady=10)
        clear_button = Button(self.main_frame, text="clear tasks", fg='black', command=self.clear, width=self.button_width, height=self.button_height)
        clear_button.pack(side=TOP, pady=10)

    #destroy a frame
    def clear_all_frames(self):
        for widget in self.root.winfo_children():
            if widget != self.main_frame:
                widget.destroy()
    
    #Adds the task to the text file
    def save_task(self):
        if self.selected_priority is None:
            print("priority is not set. select one")
            return
        task_text = self.task_entry.get()
        print("Task saved with priority: ", task_text, self.selected_priority)
        someTask.add(task_text, self.selected_priority)
        someTask.printInfo()
        threading.Thread(target=self.open_notepad).start()
    
    def save_index(self):
        index_text = self.index_entry.get()
        print(index_text)
        index_num = int(index_text)
        print('num: ', index_num)
        someTask.remove(index_num)
        threading.Thread(target=self.open_notepad).start()
    
    def complete_index(self):
        index_text = self.index_entry.get()
        print(index_text)
        index_num = int(index_text)
        someTask.mark_done(index_num)
        someTask.printInfo()
        threading.Thread(target=self.open_notepad).start()

    def clear(self):
        someTask.clear()
        threading.Thread(target=self.open_notepad).start()
    
    def set_priority(self, priority=None):
        # Reset the visual state of all buttons
        if self.selected_priority:
            self.reset_button_state()

        # Set the new selected button
        self.selected_priority = priority
        self.update_button_state()

        # Implement your priority setting logic here
        print(f"Priority set to {priority}")
        return priority
    
    def open_notepad(self):
        #finds notepad.exe a kill it before running next notepad
        subprocess.run(["taskkill", "/F", "/IM", "notepad.exe"])
        subprocess.Popen(['notepad', 'text.txt'])

    def update_button_state(self):
        # Change the relief of the selected button to 'sunken'
        if self.selected_priority == "Low":
            self.low_button.config(relief=SUNKEN)
        elif self.selected_priority == "Medium":
            self.medium_button.config(relief=SUNKEN)
        elif self.selected_priority == "High":
            self.high_button.config(relief=SUNKEN)

    def reset_button_state(self):
        # Reset the relief of all buttons to 'raised'
        self.low_button.config(relief=RAISED)
        self.medium_button.config(relief=RAISED)
        self.high_button.config(relief=RAISED)

