from planner import Planner

def main_menu():
    print("Welcome to the Agile Planner")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Exit")

def add_task_ui(planner):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    planner.add_task(title, description, due_date)
    print("Task added successfully.")

def list_tasks_ui(planner):
    planner.list_tasks()

def complete_task_ui(planner):
    index = int(input("Enter task index to mark as completed: ")) - 1
    planner.complete_task(index)

def run():
    planner = Planner()
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task_ui(planner)
        elif choice == '2':
            list_tasks_ui(planner)
        elif choice == '3':
            complete_task_ui(planner)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run()