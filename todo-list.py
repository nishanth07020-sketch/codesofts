tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['task']} - {task['status']}")

def add_task():
    task_name = input("\nEnter task name: ")
    tasks.append({"task": task_name, "status": "Pending"})
    print("Task added successfully!")

def update_task():
    show_tasks()
    task_no = int(input("\nEnter task number to update: "))
    if 1 <= task_no <= len(tasks):
        new_task = input("Enter new task name: ")
        tasks[task_no - 1]["task"] = new_task
        print("Task updated successfully!")
    else:
        print("Invalid task number!")

def complete_task():
    show_tasks()
    task_no = int(input("\nEnter task number to mark complete: "))
    if 1 <= task_no <= len(tasks):
        tasks[task_no - 1]["status"] = "Completed"
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

def delete_task():
    show_tasks()
    task_no = int(input("\nEnter task number to delete: "))
    if 1 <= task_no <= len(tasks):
        tasks.pop(task_no - 1)
        print("Task deleted successfully!")
    else:
        print("Invalid task number!")

while True:
    print("\n--- TO-DO LIST APPLICATION ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Complete Task")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        complete_task()
    elif choice == "5":
        delete_task()
    elif choice == "6":
        print("Thank you for using To-Do List App!")
        break
    else:
        print("Invalid choice! Please try again.")
