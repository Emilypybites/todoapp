todos = []

def add_task():
    task = input("Enter task:")
    todos.append(task)

def view_tasks():
    if not todos:
        print("No tasks found")

    else:
        for todo in todos:
            print(todo)


from dataclasses import dataclass

@dataclass
class Todo:
    title: str
    completed: bool

todos = []

def add_todo():
    user_input = input("Add a task: ")
    todo = Todo(title=user_input, completed=False)
    todos.append(todo)

def complete_todo(number):
    todos[number - 1].completed = True

def print_todos():
    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo.title} - {todo.completed}")

add_todo()
add_todo()
print_todos()
print()
complete_todo(1)
print_todos()



