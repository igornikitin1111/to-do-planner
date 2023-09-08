import PySimpleGUI as sg


layout = [
    [sg.Text('')],
    [sg.InputText(key='-TASK-'), sg.Button('Add Task')],
    [sg.Listbox(values=[], size=(30, 5), key='-TASK-LIST-')],
    [sg.Button('Delete Task'), sg.Button('Escape'), sg.Button('Show as a table')]
    ]


window = sg.Window('To-Do List', layout)

tasks = []

table_layout = [
    [sg.Table(values=[], headings=['Task'], auto_size_columns=False, num_rows=10, key='-TABLE-')],
    [sg.Button('Back')]
]

table_window = sg.Window('Tasks list:', table_layout, finalize=True)
table_window.hide()

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Escape':
        break
    elif event == 'Add Task' and values['-TASK-']:
        task = values['-TASK-']
        tasks.append(task)
        window['-TASK-LIST-'].update(values=tasks)
        window['-TASK-'].update(value='')
    elif event == 'Delete Task':
        selected_tasks = values['-TASK-LIST-']
        if selected_tasks:
            selected_task = selected_tasks[0]
            tasks.remove(selected_task)
            window['-TASK-LIST-'].update(values=tasks)
    elif event == 'Show as a table':
        table_values = []
        for task in tasks:
            table_values.append((task,))
        table_window['-TABLE-'].update(values=table_values)
        window.hide()
        table_window.un_hide()


window.close()