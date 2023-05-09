import pickle 

def display_menu():
    """Display the menu options for the To-Do list application."""
    print("To-Do List Menu")
    print("1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Exit")

def get_user_choice():
    """Prompt the user to enter a menu option and return the choice as an integer."""
    choice = input("Enter the number of your choice: ")
    return int(choice)

def add_task(tasks):
    """Prompt the user to enter a new task and append it to the tasks list."""
    new_task = input("Enter the new task: ")
    tasks.append(new_task)
    print(f"Added task: {new_task}")

def list_tasks(tasks):
    """Display the tasks in the list along with their index numbers."""
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

def remove_task(tasks):
    """Prompt the user to enter the index number of the task to remove and remove it from the tasks list."""
    if tasks: 
        task_index = int(input("Enter the index number of the task to remove: ")) - 1
        if 0 <= task_index < len(tasks): 
            removed_task = tasks.pop(task_index)
            print(f"Removed task: {removed_task}.")
        else: 
            print("Invalid index. No task removed.")

def save_tasks(tasks, filename="tasks.pickle"): 
    """Save the tasks list to a file using the pickle module."""
    with open(filename, "wb") as file: 
        pickle.dump(tasks, file)
    print("Tasks saved to file.")

def load_tasks(filename="tasks.pickle"):
    """Load the tasks list from a file using the pickle module. If the file doesn't exist, return an empty list."""
    try: 
        with open(filename, "rb") as file:
            tasks = pickle.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks


if __name__ == "__main__":

    tasks = load_tasks()

    while True: 
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            add_task(tasks)
        elif choice == 2: 
            list_tasks(tasks)
        elif choice == 3: 
            list_tasks(tasks)
            remove_task(tasks)
        elif choice == 4: 
            save_tasks(tasks)
            print("Exiting the application.")
            break
        else: 
            print("Invalid choice. Please enter a number between 1 and 4.") 