from datetime import datetime
import threading

class task:
    def __init__(self, priority='low priority'):
        self.task_lists = self.load_tasks()
        self.priority = priority
        self.counter = int(self.get_last_index()) + 1
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
        task_list = []

        with open('text.txt', 'r', encoding='utf-8') as file:
            # Skip the header (first line)
            next(file)

            for line in file:
                parts = line.strip().split()

                # Find the index of priority keywords (Low, Medium, High)
                priority_index = next((i for i, part in enumerate(parts) if part in ['Low', 'Medium', 'High']), None)

                if priority_index is not None:
                    # Combine anything before the priority into the task
                    task = ' '.join(parts[1:priority_index])
                    
                    # Check if the last part indicates a checkmark
                    check_mark = '✓' if len(parts) > priority_index + 2 and parts[priority_index + 2] == '✓' else ''

                    task_dict = {
                        'task': task,
                        'priority': parts[priority_index],
                        'date_added': parts[priority_index + 1],
                        'check': check_mark
                    }

                # Append the task dictionary to the task_list
                task_list.append(task_dict)

        return task_list


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
                parts = last_line.split()
                last_index_str = parts[0]

                # Check if the last index is numeric
                if last_index_str.isdigit():
                    return int(last_index_str)
                else:
                    # If not numeric, return 0
                    return 0
            else:
                # If there are no lines, return 0
                return 0
    
    #Add task to the list
    def add(self, task, priority='low priority'):
        self.counter = int(self.get_last_index()) + 1
        date_added = datetime.now().strftime('%d-%m-%Y')
        check = ''  # Assuming a new task does not have a checkmark initially
        self.task_lists.append({'task': task, 'priority': priority, 'date_added': date_added, 'check': check})

        with open('text.txt', 'a') as file:
            file.write(f"{self.counter:^10}{task:^20}{priority:^15}{date_added:^20}{check:^10}\n")


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
                    checkmark = '✓' if task_info.get('check') == '✓' else ''
                    file.write(f"{i:^10}{task_info['task']:^20}{task_info['priority']:^15}{task_info['date_added']:^20}"
                           f"{checkmark:^10}\n")
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