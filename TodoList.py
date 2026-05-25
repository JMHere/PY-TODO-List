todoList = ['Homework', 'Workout']

def printTodoList():
    for i in todoList:
        print(i)

print('Your TODO List:')
printTodoList()

while True:
    print('Type (0) to exit')
    print('Type (1) to Add a TODO')
    print('Type (2) to Remove a TODO')
    userInput = input()
    if userInput == '1':
        todo = input('Enter your new TODO: ')
        todoList.append(todo)
        printTodoList()
    elif userInput == '2':
        todoLocation = input('Enter number of todo in list order: ')
        todoList.pop(int(todoLocation) - 1)
        printTodoList()
    elif userInput == '0':
        break