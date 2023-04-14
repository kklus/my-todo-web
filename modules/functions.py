FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

FREEZING_POINT=0
BOILING_POINT=100

def state_of_water(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif temperature <= BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"