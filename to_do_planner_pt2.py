import PySimpleGUI as sg
import pickle
from datetime import datetime


class Tasks:
    def __init__(self, name, description, deadline, start_time=datetime.now(), status='in progress'):
        self.name = name
        self.description = description
        self.status = status
        self.deadline = deadline
        self.start_time = start_time

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

    @classmethod
    def change_status(cls, task_name, new_status):
        for task in cls.task_list:
            if cls.name == task_name:
                cls.status == new_status
                




project = Tasks('name', datetime(2023, 9, 9, 11, 00))
green_team = Entries()
green_team.add_task(project)

main_layout = [
    [sg.Text('Type task name')],
    [sg.InputText(key='-TASK-'), sg.Button('Add Task')],
    [sg.Listbox(values=[], size=(30, 5), key='-TASK-LIST-')],
    [sg.Button('Delete Task'), sg.Button('Escape'), sg.Button('Show as a table')],
    [sg.Button('Save'), sg.Button('Load')],
    ]

window = sg.Window('To-Do List', main_layout)

task_add_layout = [
    [sg.Text("task description"), sg.InputText(key='-DESCRIPTION-')], 
    [sg.Text("task deadline(YYYY/MM/DD, HH/MM)"), sg.InputText(key='-DEADLINE-')],
    [sg.Button('Submit info')]
    ]

task_add_window = sg.Window('additional layout', task_add_layout, finalize=True)
task_add_window.hide()

table_layout = [
    [sg.Table(values=[], headings=['Task'], auto_size_columns=False, num_rows=10, key='-TABLE-')],
    [sg.Button('Back')]
    ]

table_window = sg.Window('Tasks list:', table_layout, finalize=True)
table_window.hide()
