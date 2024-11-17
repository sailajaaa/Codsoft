import json

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def mark_as_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_as_done(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

if __name__ == "__main__":
    main()