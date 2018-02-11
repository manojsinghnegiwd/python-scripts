print('Welcome to Python Todo Script')
print('You can type help to list available commands')

user_not_exited = True
todo_list = []

def add_item(user_input):
    itemText = " ".join(user_input[1:])
    todo_list.append(itemText)

def edit_item(user_input):
    print(user_input)

def list_items(user_input):
    for i in range(len(todo_list)):
        print(i+1, ' ', todo_list[i])

def delete_item(user_input):
    global todo_list

    todo_item = todo_list[int(user_input[1]) - 1] 
    if todo_item:
        todo_list.remove(todo_item)

def exit_program(user_input):
    global user_not_exited
    user_not_exited = False

def help_menu(user_input):
    for command in available_commands:
        print(command, ' : ', available_commands[command]['description'])
    

available_commands = {
    'add': {
        'description': 'Add items to todo - add [your todo item]',
        'execute': add_item
    },
    'edit': {
        'description': 'Edit items in todo - edit [index] [modified todo item]',
        'execute': edit_item
    },
    'list': {
        'description': 'List all todos - list',
        'execute': list_items
    },
    'delete': {
        'description': 'Delete items from todo - delete [index]',
        'execute': delete_item
    },
    'exit': {
        'description': 'Exit Python Todo Script',
        'execute': exit_program
    },
    'help': {
        'description': 'Print help menu',
        'execute': help_menu
    }
}

def repl():
    
    while user_not_exited:
        user_input = input('> ')

        if user_input != '':
            splitted_input = user_input.split(' ')
            command_to_exec = available_commands[splitted_input[0]]
            command_to_exec['execute'](splitted_input)


repl()


