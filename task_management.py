import csv

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

class TaskManager(Task):
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority):
        task = Task(title, priority)
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        pending_tasks = [task for task in self.tasks if not task.completed]
        if not pending_tasks:
            print("No pending tasks.")
            return
        for index, task in enumerate(pending_tasks, start=1):
            print(f"{index}. {task.title} - Priority: {task.priority} - Completed: {'Yes' if task.completed else 'No'}")

    def complete_task(self, task_index):
        if task_index < 0 or task_index >= len(self.tasks):
            print("Invalid task index.")
            return
        pending_tasks = [task for task in self.tasks if not task.completed]
        if task_index >= len(pending_tasks):
            print("Invalid task index.")
            return
        task = pending_tasks[task_index]
        task.mark_completed()
        print("Task marked as completed.")
        self.view_tasks() 

    def view_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.completed]
        if completed_tasks:
            for index, task in enumerate(completed_tasks, start=1):
                print(f"{index}. {task.title} - Priority: {task.priority}")
        else:
            print("No completed tasks.")

    def save_tasks_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task.title, task.priority, task.completed])

    def load_tasks_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 3:
                        title, priority, completed = row
                        task = Task(title, priority)
                        task.completed = completed == 'True'
                        self.tasks.append(task)
                    else:
                        print("Invalid data format in the tasks file.")
        except FileNotFoundError:
            print("No tasks file found.")

def main():
    task_manager = TaskManager()
    task_manager.load_tasks_from_file("tasks.csv")

    while True:
        print("\n🟡🟢🟠 Task Management System 🟠🟢🟡")
        print("1. Add New Task ➕")
        print("2. View Tasks 👁‍🗨")
        print("3. Complete Task ✔")
        print("4. View Completed Tasks✅")
        print("5. Exit ❌")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            priority = input("Enter task priority (high/medium/low): ")
            task_manager.add_task(title, priority)

        elif choice == "2":
            task_manager.view_tasks()

        elif choice == "3":
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            task_manager.complete_task(task_index)

        elif choice == "4":
            task_manager.view_completed_tasks()

        elif choice == "5":
            task_manager.save_tasks_to_file("tasks.csv")
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()
