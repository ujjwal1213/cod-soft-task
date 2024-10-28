import json
import os
from datetime import datetime

class TodoList:
    def _init_(self, filename='todo.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title, priority='low'):
        task = {
            'title': title,
            'completed': False,
            'priority': priority,
            'created_at': str(datetime.now())
        }
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = '✔' if task['completed'] else '❌'
            print(f"{index}. [{status}] {task['title']} (Priority: {task['priority']})")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()

def main():
    todo_list = TodoList()

    while True:
        print("\n--- To-Do List ---")
        todo_list.view_tasks()
        print("\nOptions:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (low, medium, high): ")
            todo_list.add_task(title, priority)
        elif choice == '2':
            task_index = int(input("Enter task number to complete: ")) - 1
            todo_list.complete_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '_main_':
    main()