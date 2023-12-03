from tkinter import *
from tasks import task

someTask = task()

class GUIManagers:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x300")

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

        clear_button = Button(self.main_frame, text="clear tasks", fg='black', command=someTask.clear, width=self.button_width, height=self.button_height)
        clear_button.pack(side=TOP, pady=10)

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

        #something to reference in the show_main_screen
        self.alternate_frame = alternate_frame

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

        clear_button = Button(self.main_frame, text="clear tasks", fg='black', command=someTask.clear, width=self.button_width, height=self.button_height)
        clear_button.pack(side=TOP, pady=10)
    def clear_all_frames(self):
        for widget in self.root.winfo_children():
            if widget != self.main_frame:
                widget.destroy()
    def save_task(self):
        task_text = self.task_entry.get()
        print("Task saved: ", task_text)
        someTask.add(task_text)
    def save_index(self):
        index_text = self.index_entry.get()
        print(index_text)
        index_num = int(index_text)
        print('num: ', index_num)
        someTask.remove(index_num)
    def complete_index(self):
        index_text = self.index_entry.get()
        print(index_text)
        index_num = int(index_text)
        someTask.mark_done(index_num)
