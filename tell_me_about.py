print('Welcome to Tell Me About Python script')
print('You can type anything from a person name to a topic name.')
print('This script search wikipedia for the information and display it here.')
print("Let's get started ... ")
print(40*'*')

user_not_exited = True

def repl():
    global user_not_exited

    while user_not_exited:
        user_input = input('> ')

        if user_input == 'exit':
            user_not_exited = False

        print(user_input)

repl()
