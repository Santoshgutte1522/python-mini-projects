tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def display_tasks():
    if not tasks:
        print("No tasks available!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task():
    display_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task deleted!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")


while True:
    print("\n1. Add Task\n2. Display Tasks\n3. Delete Task\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        display_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
