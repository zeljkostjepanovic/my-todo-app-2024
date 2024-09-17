import os
import time
from modules import functions

### Make sure to run the program in the same working directory where the script is located
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

### Main loop
while True:
    user_action = input("Type add, show, edit, complete or exit: ").lower().strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
            
        todos = functions.get_todos()
        
        if len(todo) > 1:
            todos.append(todo)
            functions.write_todos(todos)              
        else:
           print("Empty task?")
           continue
            
    elif user_action.startswith("show"):
        todos = functions.get_todos()
                        
        for index,item in enumerate(todos, start=1):
            item = item.strip("\n")
            row = f"{index}-{item}"
            print(row)
            
    elif user_action.startswith("edit"):
        try:
            todos = functions.get_todos()
        
            for index,item in enumerate(todos, start=1):
                item = item.strip("\n")
                row = f"{index}-{item}"
                print(row)
        
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            
            functions.write_todos(todos)
        except:
            print("Try again.")
            continue
        
    elif user_action.startswith("complete"):
        try:
            todos = functions.get_todos()

            
            for index,item in enumerate(todos, start=1):
                item = item.strip("\n")
                row = f"{index}-{item}"
                print(row)
                
            number = int(input("Which one is completed? "))
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)         
                
            functions.write_todos(todos)   
                
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except:
            print("Command not valid, try again.")
            continue
        
    elif user_action.startswith("exit"):
        break

    else:
        print("Didn't understand that.")

print("Bye!")
exit()