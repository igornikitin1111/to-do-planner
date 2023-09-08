import pickle
from datetime import datetime

#klaidu gaudymas -- Igor

class Task:
    def __init__(self, name, description, deadline, start_time=datetime.now(), status='in progress'):
        self.name = name
        self.description = description
        self.start_time = start_time
        self.status = status
        self.deadline = deadline

    def __str__(self) -> str:
        return(f'{self.name}, {self.status}')


class Entries:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def delete_task(self, task_name):
        for task in self.task_list:
            if task.name == task_name:
                self.task_list.remove(task)

    def save_to_pickle(self, filename):
        with open (filename, 'wb') as file:
            pickle.dump(self.task_list, file)
            
    def load_from_pickle(self, filename):
        with open(filename, 'rb') as file:
            self.task_list = pickle.load(file)


    def change_status(self, task_name, new_status):
        for task in self.task_list:
            if task.name == task_name:
                task.status = new_status

    def change_deadline(self, task_name, new_deadline):
        for task in self.task_list:
            if task.name == task_name:
                task.deadline == new_deadline
        
                

