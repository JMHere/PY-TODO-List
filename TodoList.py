import json

fileName = 'todo_list.json'

try:
    with open(fileName, 'r') as f:
        todoList = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    todoList = []


def printTodoList():
    for todo in todoList:
        status = ''
        if todo['completed'] == False:
            status = 'Not done'
        else:
            status = 'Done'
        print(todo['todo'] + ' : ' + status)

print('Your TODO List:')
printTodoList()

while True:
    print('Type (0) to Exit')
    print('Type (1) to Add a TODO')
    print('Type (2) to Update TODO')
    print('Type (3) to Remove a TODO')
    userInput = input()
    if userInput == '1':
        todo = input('Enter your new TODO: ')
        todo = { 'todo' : todo, 'completed' : False }
        todoList.append(todo)
        printTodoList()
    elif userInput == '2':
        index = input('Enter number of todo in list order: ')
        # setting the index to 0 base for more user-friendly input
        index = int(index) - 1
        # toggle completion status instead of setting it manually
        todoList[index]['completed'] = not todoList[index]['completed']
        printTodoList()
    elif userInput == '3':
        index = input('Enter number of todo in list order: ')
        todoList.pop(int(index) - 1)
        printTodoList()
    elif userInput == '0':
        break

with open(fileName, 'w') as f:
    json.dump(todoList, f)