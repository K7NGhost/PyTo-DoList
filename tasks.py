from datetime import datetime
import threading
import re

class task:
    def __init__(self, priority='low priority'):
        self.task_lists = self.load_tasks()
        self.priority = priority
        self.counter = self.get_last_index() + 1
        self.file_lock = threading.Lock()

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
                file.write(f"{'Index':^10}{'Task':^20}{'Priority':^15}{'Date Added':^20}{'Check':^10}\n")

    def load_tasks(self):
        tasks = []
        try:
            with open('text.txt', 'r') as file:
                # Skip the header line
                file.readline()
                lines = file.readlines()
                for i, line in enumerate(lines, start=1):
                    # Use regular expression to extract the task name
                    match = re.match(r'^\s*(\d+)\s+(.*?)\s+(\S+)\s+(\S+)\s*$', line)
                    if match:
                        index, task, priority, date_added = match.groups()
                        check = '✓' if '✓' in line else ''
                        tasks.append({'task': task, 'priority': priority, 'date_added': date_added, 'check': check})
        except FileNotFoundError:
            pass
        return tasks


    #grabs the last index in the list
    def get_last_index(self):
        with open('text.txt', 'r') as file:
            # Read the header line
            file.readline()
            lines = file.readlines()

            # Check if there are any lines in the file
            if lines:
                # Get the last line and extract the index
                last_line = lines[-1]
                last_index = int(last_line.split()[0])
                return last_index
            else:
                # If there are no lines, return 0
                return 0
    
    #Add task to the list
    def add(self, task, priority='low priority'):
        date_added = datetime.now().strftime('%d-%m-%Y')
        self.task_lists.append({'task': task, 'priority':priority, 'date_added': date_added})
        with open('text.txt', 'a') as file:
            file.write(f"{self.counter:^10}{task:^20}{priority:^15}{date_added:^20}{' ':^10}\n")
        self.counter += 1

    #remove a task based on the index num
    def remove(self, index):
        if 1 <= index <= len(self.task_lists):
            removed_task = self.task_lists.pop(index - 1)

            with open('text.txt', 'w', encoding='utf-8') as file:
                file.write(f"{'Index':^10}{'Task':^20}{'Priority':^15}{'Date Added':^20}{'Check':^10}\n")
                for i, task_info in enumerate(self.task_lists, start=1):
                    checkmark = '✓' if 'check' in task_info and task_info['check'] == '✓' else ' '
                    file.write(f"{i:^10}{task_info['task']:^20}{task_info['priority']:^15}{task_info['date_added']:^20}"f"{checkmark:^10}\n")
            return removed_task
        else:
            print("Invalid index. Please provide a valid index")
    
    #mark done function self explanatory
    def mark_done(self, index):
        if 1 <= index <= len(self.task_lists):
        # Update the 'check' field for the specified task index
            self.task_lists[index - 1]['check'] = '✓'

            with open('text.txt', 'w', encoding='utf-8') as file:
                file.write(f"{'Index':^10}{'Task':^20}{'Priority':^15}{'Date Added':^20}{'Check':^10}\n")
                for i, task_info in enumerate(self.task_lists, start=1):
                    checkmark = task_info.get('check', ' ')
                    file.write(f"{i:^10}{task_info['task']:^20}{task_info['priority']:^15}{task_info['date_added']:^20}"f"{checkmark:^10}\n")
        else:
            print("Invalid index. Please provide a valid index")

    #prints the items in the list used for debugging purposes
    def printInfo(self):
        print(f'The tasks in the list are {self.task_lists}')
        print(f'The priority of these tasks are {self.priority}')

    #clears the text file
    def clear(self):
        self.task_lists = []
        with open('text.txt', 'w') as file:
            pass
        with open('text.txt', 'a') as file:
            file.write(f"{'Index':^10}{'Task':^20}{'Priority':^15}{'Date Added':^20}{'Check':^10}\n")
        self.counter = 1