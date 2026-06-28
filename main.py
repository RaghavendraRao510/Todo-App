import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\nTo-Do List")
    print("-" * 30)

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

    print()


def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.\n")


def complete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        num = int(input("Task number: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task completed.\n")
    except:
        print("Invalid task number.\n")


def delete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        num = int(input("Task number: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted.\n")
    except:
        print("Invalid task number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO APP =====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()