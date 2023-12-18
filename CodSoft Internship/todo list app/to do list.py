class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def remove_task(self, task):
        try:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the list.")
        except ValueError:
            print(f"Task '{task}' not found in the list.")

    def show_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Your To-Do list is empty.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Show all tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            to_do_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task you want to remove: ")
            to_do_list.remove_task(task)
        elif choice == '3':
            to_do_list.show_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def remove_task(self, task):
        try:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the list.")
        except ValueError:
            print(f"Task '{task}' not found in the list.")

    def show_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("Your To-Do list is empty.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Show all tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            to_do_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task you want to remove: ")
            to_do_list.remove_task(task)
        elif choice == '3':
            to_do_list.show_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


