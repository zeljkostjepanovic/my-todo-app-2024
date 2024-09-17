FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return list of todos

    Args:
        filepath (string): path of the text file with saved todos,
        with each todo in a separate line

    Returns:
        list: returns a list of strings (todos)
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(content, filepath=FILEPATH):
    """ Write a list of todos to a file

    Args:
        filepath (string): Path of the file where todos are saved
        content (list): List of todos to write to file, one line for each
    """
    with open(filepath, 'w') as file:
        file.writelines(content)   