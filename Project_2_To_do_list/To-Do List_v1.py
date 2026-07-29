tasks = []
completed=[]

def show_task():
    if len(tasks) == 0:
        print("No task available")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, 1):
            if i in completed:
                print("status=",✅)
            else:
                print("status=",❌)
            print(f"{i}.{status} {task}")            

def add_task():
    a = input("Enter task: ")
    tasks.append(a)
    print("Task added ")

def delete_task():
    show_task()
    if len(tasks) == 0:
        return
    b = int(input("Enter the task number to delete: "))
    if b == 0:
        return
    elif 1 <= b <= len(tasks): 
        removed = tasks.pop(b-1)
        print(f"Deleted: {removed} ")
    else:
        print("Task not found")

while True:
    print("\nMain menu")
    print("1. Show task")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")
    
    c = int(input("Enter your choice: "))
    
    if c == 1:
        show_task()
    elif c == 2:
        add_task()
    elif c == 3:
        delete_task()
    elif c == 4:
        print("Exit")
        break
    else:
        print("Invalid")
