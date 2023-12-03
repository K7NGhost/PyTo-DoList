
class task:
    def __init__(self, task_lists=[], priority='low priority'):
        self.task_lists = task_lists
        self.priority = priority
        
    def add(self, task):
        self.task_lists.append(task)
        with open('text.txt', 'w') as file:
            for items in self.task_lists:
                file.write(items + '\n')
    
    def printInfo(self):
        print(f'The tasks in the list are {self.task_lists}')
        print(f'The priority of these tasks are {self.priority}')