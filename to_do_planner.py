import PySimpleGUI as sg
import pickle
from datetime import datetime


class Tasks:
    def __init__(self, name, status, deadline, start_time=datetime.now()):
        self.name = name
        self.start_time = start_time
        self.status = status
        self.deadline = deadline
        self.task_list = []
    
    def save_to_pickle(self, filename):
        with open (filename, 'wb') as file:
            pickle.dump(self.task_list, file)
            
    def load_from_pickle(self, filename):
        with open(filename, 'rb') as file:
            self.task_list = pickle.load(file)


project = Tasks('name', 'status', '2023/09/09 11:00')


layout = [
    [sg.Text('')],
    [sg.InputText(key='-TASK-'), sg.Button('Add Task')],
    [sg.Listbox(values=[], size=(30, 5), key='-TASK-LIST-')],
    [sg.Button('Delete Task'), sg.Button('Escape'), sg.Button('Show as a table')],
    [sg.Button('Save'), sg.Button('Load')],
    ]


window = sg.Window('To-Do List', layout)

table_layout = [
    [sg.Table(values=[], headings=['Task'], auto_size_columns=False, num_rows=10, key='-TABLE-')],
    [sg.Button('Back')]
]

table_window = sg.Window('Tasks list:', table_layout, finalize=True)
table_window.hide()

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Escape':
        project.save_to_pickle('autosave_todo.pkl')
        break
    elif event == 'Add Task' and values['-TASK-']:
        task = values['-TASK-']
        project.task_list.append(task)
        window['-TASK-LIST-'].update(values=project.task_list)
        window['-TASK-'].update(value='')
    elif event == 'Delete Task':
        selected_tasks = values['-TASK-LIST-']
        if selected_tasks:
            selected_task = selected_tasks[0]
            project.task_list.remove(selected_task)
            window['-TASK-LIST-'].update(values=project.task_list)
    elif event == 'Save':
        project.save_to_pickle('todo.pkl')
    elif event == 'Load':
        project.load_from_pickle('todo.pkl')
        window['-TASK-LIST-'].update(values=project.task_list)
    elif event == 'Show as a table':
        table_values = []
        for task in project.task_list:
            table_values.append(task)
        table_window['-TABLE-'].update(values=table_values)
        window.hide()
        table_window.un_hide()
        table_event, table_values = table_window.read()
        if table_event == 'Back':
            table_window.hide()
            window.un_hide()


window.close()