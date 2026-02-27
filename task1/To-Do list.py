import os

def clear_screen():
    """Clears the terminal for a cleaner look."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("\n--- YOUR PERSONAL TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Mark Task as Done")
    print("4. Remove a Task")
    print("5. Exit")
    print("--------------------------------")

def main():
    tasks = []
    
    while True:
        show_menu()
        choice = input("What would you like to do? (1-5): ")

        if choice == '1':
            clear_screen()
            print("--- CURRENT TASKS ---")
            if not tasks:
                print("Your list is empty. Take a break!")
            else:
                for index, task in enumerate(tasks, start=1):
                    status = "✔" if task['done'] else " "
                    print(f"{index}. [{status}] {task['name']}")
            
        elif choice == '2':
            new_task = input("Enter the task name: ")
            if new_task.strip():
                tasks.append({'name': new_task, 'done': False})
                print(f"Added: {new_task}")
            else:
                print("Task name cannot be empty!")

        elif choice == '3':
            # Marking a task as complete
            try:
                task_num = int(input("Enter the task number to mark as done: "))
                tasks[task_num - 1]['done'] = True
                print("Great job on finishing that task!")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == '4':
            # Removing a task from the list
            try:
                task_num = int(input("Enter the task number to remove: "))
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed['name']}")
            except (ValueError, IndexError):
                print("Invalid task number.")

        elif choice == '5':
            print("Goodbye! Stay productive.")
            break

        else:
            print("Oops! That's not a valid option. Please try again.")

if __name__ == "__main__":
    main()
