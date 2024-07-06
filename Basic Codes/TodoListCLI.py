class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added:", task)

    def show_tasks(self):
        print("Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

if __name__ == "__main__":
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.show_tasks()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
