import PySimpleGUI as sg
import pickle
from datetime import datetime

#padaryt tvarkinga lentele
#pagerint grafine vartotojo sasaja
#padaryt funkcionalius deadline ir status pakeitimus
#klaidu gaudymas

class Tasks:
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

    @classmethod
    def change_status(cls, task_name, new_status):
        for task in cls.task_list:
            if task.name == task_name:
                task.status = new_status


    @classmethod
    def change_deadline(cls, task_name, new_deadline):
        for task in cls.task_list:
            if task.name == task_name:
                task.deadline == new_deadline
        
                


green_team = Entries()

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
    [sg.Text("task deadline(YYYY/MM/DD, HH:MM)"), sg.InputText(key='-DEADLINE-')],
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

while True:
    main_event, main_values = window.read()

    if main_event == sg.WINDOW_CLOSED or main_event == 'Escape':
        green_team.save_to_pickle('autosave_todo.pkl')
        break

    elif main_event == 'Add Task' and main_values['-TASK-']:
        window.hide()
        task_add_window.un_hide()
        task_add_event, task_add_values = task_add_window.read()

        if task_add_event == 'Submit info':
            task = Tasks(main_values['-TASK-'], task_add_values['-DESCRIPTION-'], task_add_values['-DEADLINE-'])
            green_team.add_task(task)
            task_add_window['-DESCRIPTION-'].update(value='')
            task_add_window['-DEADLINE-'].update(value='')
        task_add_window.hide()
        window.un_hide()

        window['-TASK-LIST-'].update(values=green_team.task_list)
        window['-TASK-'].update(value='')


    elif main_event == 'Delete Task':
        selected_tasks = main_values['-TASK-LIST-']

        if selected_tasks:
            selected_task = selected_tasks[0]
            green_team.task_list.remove(selected_task)
            window['-TASK-LIST-'].update(values=green_team.task_list)

    elif main_event == 'Save':
        green_team.save_to_pickle('todo.pkl')

    elif main_event == 'Load':
        green_team.load_from_pickle('todo.pkl')
        window['-TASK-LIST-'].update(values=green_team.task_list)

    elif main_event == 'Show as a table':
        table_values = []
        for task in green_team.task_list:
            table_values.append(task)
        table_window['-TABLE-'].update(values=table_values)
        window.hide()
        table_window.un_hide()
        table_event, table_values = table_window.read()

        if table_event == 'Back':
            table_window.hide()
            window.un_hide()


window.close()