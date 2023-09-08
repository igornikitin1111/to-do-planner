layout = [
    [sg.Text('')],
    [sg.InputText(key='-TASK-'), sg.Button('Add task')],
    [sg.Listbox(values=[], size=(30, 5), key='-TASK-LIST-')],
    [sg.Button('Delete Task'), sg.Button('Escape')]
]

window = sg.Window('To-Do List', layout)
tasks = [] 

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

window.close()