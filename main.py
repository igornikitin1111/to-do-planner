from back import Entries, Task
import PySimpleGUI as sg
from datetime import datetime


# padaryt tvarkinga lentele -- Ilya
# pagerint grafine vartotojo sasaja -- Deivida

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
    [sg.Text("Task description"), sg.InputText(key='-DESCRIPTION-')],
    [sg.Text("Task deadline (YYYY/MM/DD, HH:MM)"), sg.InputText(key='-DEADLINE-')],
    [sg.Button('Submit info')]
]

task_add_window = sg.Window('Additional layout', task_add_layout, finalize=True)
task_add_window.hide()

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
            task = Task(main_values['-TASK-'], task_add_values['-DESCRIPTION-'], task_add_values['-DEADLINE-'])
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
            if isinstance(task.deadline, str):
                try:
                    task.deadline = datetime.strptime(task.deadline, '%Y/%m/%d, %H:%M')
                except ValueError:
                    task.deadline = datetime.strptime(task.deadline, '%Y-%m-%d %H:%M:%S')
            time_left = task.deadline - datetime.now().replace(microsecond=0)
            table_values.append([task.name, task.description, str(time_left), task.status])

        table_layout = [
            [
                sg.Table(
                    values=table_values,
                    headings=['Task name', 'Description', 'Time left to Deadline', 'Status'],
                    auto_size_columns=True,
                    num_rows=10,
                    key='-TABLE-',
                    text_color='black',
                    justification='center',
                )
            ],
            [sg.Button('Back')]
        ]

        table_window = sg.Window('Tasks table', table_layout, finalize=True)

        while True:
            table_event, table_values = table_window.read()

            if table_event == 'Back' or table_event == sg.WIN_CLOSED:
                break
        
        table_window.close()
        window.un_hide()

window.close()