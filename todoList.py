
def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file if line.strip()]
        return tasks
    except FileNotFoundError:
        return []
    
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

#Function to show the current list
def show_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

#Main function to run the menu and get the input from the user
def main():
    tasks = load_tasks()

    while True:
        show_tasks(tasks)
        print("\nOptions:\n1. Add task\n2. Delete task\n3. Save tasks\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == '2':
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    print(f"Task '{removed_task}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            save_tasks(tasks)
            print("Tasks saved successfully.")
        elif choice == '4':
            save_tasks(tasks)
            print("Exiting the program. Tasks saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()