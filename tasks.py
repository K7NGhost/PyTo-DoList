from datetime import datetime

class task:
    def __init__(self, task_lists=[], priority='low priority'):
        self.task_lists = task_lists
        self.priority = priority
        self.counter = self.get_last_index() + 1

        #checks to see if header is already there
        header_exists = False
        try:
            with open('text.txt', 'r') as file:
                first_line = file.readline()
                header_exists = "Index" in first_line and "Task" in first_line and "Priority" in first_line
        except FileNotFoundError:
            pass
        
        #if header does not exist create it
        if not header_exists:
            with open('text.txt', 'a') as file:
                file.write(f"{'Index':^15}{'Task':^20}{'Priority':^15}{'Date Added':^20}\n")

    def get_last_index(self):
        with open('text.txt', 'r') as file:
            file.readline()
            last_line = file.readlines()[-1]
            last_index = int(last_line.split()[0])
            return last_index
        
    def add(self, task, priority='low priority'):
        date_added = datetime.now().strftime('%d-%m-%Y')
        self.task_lists.append({'task': task, 'priority':priority, 'date_added': date_added})
        with open('text.txt', 'a') as file:
            file.write(f"{self.counter:^5}{task:^20}{priority:^15}{date_added:^20}\n")
        self.counter += 1

    def remove(self, index):
        if 1 <= index <= len(self.task_lists):
            removed_task = self.task_lists.pop(index - 1)

            with open('text.txt', 'w') as file:
                file.write(f"{'Index':^10}{'Task':^20}{'|Priority':^15}{'|Date Added':^20}\n")
                for i, task_info in enumerate(self.task_lists, start=1):
                    file.write(f"{i:^10}{task_info['task']:^20}{task_info['priority']:^15}{task_info['date_added']:^20}\n")
            return removed_task
        else:
            print("Invalid index. Please provide a valid index")

    def printInfo(self):
        print(f'The tasks in the list are {self.task_lists}')
        print(f'The priority of these tasks are {self.priority}')

    #clears the text file
    def clear(self):
        with open('text.txt', 'w') as file:
            pass
        with open('text.txt', 'a') as file:
            file.write(f"{'Index':^5}{'Task':^20}{'Priority':^15}{'Date Added':^20}\n")
        self.counter = 1