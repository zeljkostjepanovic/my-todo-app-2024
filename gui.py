from modules import functions
import PySimpleGUI as sg
import os
import time

sg.theme('SystemDefaultForReal')
### Make sure to run the program in the same working directory where the script is located
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

clock = sg.Text('', key = 'clock')
label = sg.Text('Type in a task')
input_box = sg.InputText(tooltip="Enter todo", key="todo")

add_button = sg.Button(image_source="add.png",
                       mouseover_colors="lightblue", 
                       tooltip="Add a task", key="Add")

list_box = sg.Listbox(values=functions.get_todos(), key="todos", 
                      enable_events=True, size=(50,15))

edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]

window = sg.Window('My TODOS', 
                   layout=layout,
                   font=("Ubuntu", 9))

while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime("%H:%M:%S"))
    print("1 ", event)
    print("2 ", values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            if values['todo'] != "":
                new_todo = values['todo']+"\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            else:
                sg.popup("Please enter a task to add.")

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
        
                window['todos'].update(values=todos)
            except IndexError as e:
                sg.popup("Please select a task")
                continue

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a task")
                continue
        
        case 'Exit':
            break
        
        case 'todos':
            window['todo'].update(value=values['todos'][0])
             
        case sg.WIN_CLOSED:
            break


window.close()