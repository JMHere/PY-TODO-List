import json
import tkinter as tk

fileName = 'todo_list.json'
testList = ['Hello']

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

# while True:
#     print('Type (0) to Exit')
#     print('Type (1) to Add a TODO')
#     print('Type (2) to Update TODO')
#     print('Type (3) to Remove a TODO')
#     userInput = input()
#     if userInput == '1':
#         todo = input('Enter your new TODO: ')
#         todo = { 'todo' : todo, 'completed' : False }
#         todoList.append(todo)
#         printTodoList()
#     elif userInput == '2':
#         index = input('Enter number of todo in list order: ')
#         # setting the index to 0 base for more user-friendly input
#         index = int(index) - 1
#         # toggle completion status instead of setting it manually
#         todoList[index]['completed'] = not todoList[index]['completed']
#         printTodoList()
#     elif userInput == '3':
#         index = input('Enter number of todo in list order: ')
#         todoList.pop(int(index) - 1)
#         printTodoList()
#     elif userInput == '0':
#         break


def updateListDisplay():
    
    for widget in displayFrame.winfo_children():
        widget.destroy()

    for index, item in enumerate(todoList):
        lbl = tk.Label(displayFrame, text=item['todo'])
        lbl.grid(row=index, column=0)
        var = tk.BooleanVar(value=item['completed'])
        btn = tk.Checkbutton(displayFrame, variable=var, command=lambda idx= index, v= var : updateTodoStatus(idx, v))
        btn.grid(row=index, column=1)
        delBtn = tk.Button(displayFrame, text="Del", command=lambda idx= index : removeTodo(idx))
        delBtn.grid(row=index, column=2)

def addTodo():
    text = entry.get()
    todo = { 'todo' : text, 'completed' : False }
    if text:
        todoList.append(todo)
        updateListDisplay()
    entry.delete(0, tk.END)

def updateTodoStatus(index, var):
    todoList[index]['completed'] = var.get()
    updateListDisplay()

def removeTodo(index):
    todoList.pop(index)
    updateListDisplay()

root = tk.Tk()

root.geometry('400x200')

root.title("TODO List")

displayFrame = tk.Frame(root)
displayFrame.pack()

inputFrame = tk.Frame(root)
inputFrame.pack()
entry = tk.Entry(inputFrame)
entry.grid(row=0, column=0, padx=10)
addButton = tk.Button(inputFrame, text="Add Todo", command=addTodo)
addButton.grid(row=0,column=1, padx=10)

updateListDisplay()

root.mainloop()

with open(fileName, 'w') as f:
    json.dump(todoList, f)