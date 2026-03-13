## Vector
class Vector:
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return f"vector{self.args}"
    def __add__(self, other):
        if len(self.args) != len(other.args):
            raise ValueError("Vectors must have same dimensions to add")
        return Vector(*(a + b for a, b in zip(self.args, other.args)))
    def __sub__(self, other):
        if len(self.args) != len(other.args):
            raise ValueError("Vectors must have same dimensions")
        return Vector(*(a - b for a, b in zip(self.args, other.args)))
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.args))
        elif isinstance(other, Vector):
            if len(self.args) != len(other.args):
                raise ValueError("Vectors must have same dimensions")
            return sum(a * b for a, b in zip(self.args, other.args))
        else:
            raise TypeError("Unsupported multiplication")
    def magnitude(self):
        return (sum(a**2 for a in self.args)**0.5)
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(*(a / mag for a in self.args))
    
##  Employee Records Manager (OOP Version)
import os

# ---------------- Employee Class ----------------
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


# ---------------- Employee Manager Class ----------------
class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        # agar file mavjud bo‘lmasa, yaratamiz
        if not os.path.exists(self.FILE_NAME):
            open(self.FILE_NAME, "w").close()

    # ---- Add Employee ----
    def add_employee(self, employee):
        # unique ID tekshirish
        if self.search_employee(employee.employee_id):
            print("Error: Employee ID already exists!")
            return

        with open(self.FILE_NAME, "a") as f:
            f.write(str(employee) + "\n")
        print("Employee added successfully!")

    # ---- View All Employees ----
    def view_all_employees(self):
        print("Employee Records:")
        with open(self.FILE_NAME, "r") as f:
            lines = f.readlines()
            if not lines:
                print("No records found.")
            else:
                for line in lines:
                    print(line.strip())

    # ---- Search Employee ----
    def search_employee(self, employee_id):
        with open(self.FILE_NAME, "r") as f:
            for line in f:
                record = line.strip().split(", ")
                if record[0] == employee_id:
                    return Employee(*record)
        return None

    # ---- Update Employee ----
    def update_employee(self, employee_id, name=None, position=None, salary=None):
        updated = False
        with open(self.FILE_NAME, "r") as f:
            lines = f.readlines()

        with open(self.FILE_NAME, "w") as f:
            for line in lines:
                record = line.strip().split(", ")
                if record[0] == employee_id:
                    record[1] = name if name else record[1]
                    record[2] = position if position else record[2]
                    record[3] = salary if salary else record[3]
                    updated = True
                f.write(", ".join(record) + "\n")

        if updated:
            print("Employee updated successfully!")
        else:
            print("Employee not found.")

    # ---- Delete Employee ----
    def delete_employee(self, employee_id):
        deleted = False
        with open(self.FILE_NAME, "r") as f:
            lines = f.readlines()

        with open(self.FILE_NAME, "w") as f:
            for line in lines:
                record = line.strip().split(", ")
                if record[0] != employee_id:
                    f.write(line)
                else:
                    deleted = True

        if deleted:
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    # ---- Menu ----
    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                eid = input("Enter Employee ID: ").strip()
                name = input("Enter Name: ").strip()
                position = input("Enter Position: ").strip()
                salary = input("Enter Salary: ").strip()
                self.add_employee(Employee(eid, name, position, salary))
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                eid = input("Enter Employee ID to search: ").strip()
                emp = self.search_employee(eid)
                if emp:
                    print("Employee Found:")
                    print(emp)
                else:
                    print("Employee not found.")
            elif choice == "4":
                eid = input("Enter Employee ID to update: ").strip()
                name = input("Enter new Name (leave blank to skip): ").strip()
                position = input("Enter new Position (leave blank to skip): ").strip()
                salary = input("Enter new Salary (leave blank to skip): ").strip()
                name = name if name else None
                position = position if position else None
                salary = salary if salary else None
                self.update_employee(eid, name, position, salary)
            elif choice == "5":
                eid = input("Enter Employee ID to delete: ").strip()
                self.delete_employee(eid)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


# ---------------- Main ----------------
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()

## To-Do Application

import csv
from datetime import datetime

# ---------------- Task Class ----------------
class Task:
    def __init__(self, task_id, title, description, due_date="", status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Task(data["task_id"], data["title"], data["description"], data.get("due_date",""), data.get("status","Pending"))


# ---------------- File Handler Base Class ----------------
class TaskFileHandler:
    def save_tasks(self, tasks, filename):
        raise NotImplementedError

    def load_tasks(self, filename):
        raise NotImplementedError


# ---------------- CSV File Handler ----------------
class CSVTaskFileHandler(TaskFileHandler):
    def save_tasks(self, tasks, filename):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["task_id","title","description","due_date","status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load_tasks(self, filename):
        tasks = []
        try:
            with open(filename, "r", newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tasks.append(Task.from_dict(row))
        except FileNotFoundError:
            pass
        return tasks


# ---------------- Task Manager Class ----------------
class TaskManager:
    def __init__(self, file_handler, filename):
        self.file_handler = file_handler  # polymorphic handler (CSV/JSON/others)
        self.filename = filename
        self.tasks = self.file_handler.load_tasks(filename)

    # Add a new task
    def add_task(self, task):
        if any(t.task_id == task.task_id for t in self.tasks):
            print("Error: Task ID already exists!")
            return
        self.tasks.append(task)
        print("Task added successfully!")

    # View all tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        print("Tasks:")
        for task in self.tasks:
            print(task)

    # Update a task
    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title if title else task.title
                task.description = description if description else task.description
                task.due_date = due_date if due_date else task.due_date
                task.status = status if status else task.status
                print("Task updated successfully!")
                return
        print("Task not found.")

    # Delete a task
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found.")

    # Filter tasks by status
    def filter_tasks(self, status):
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered:
            print(f"No tasks with status '{status}' found.")
            return
        print(f"Tasks with status '{status}':")
        for task in filtered:
            print(task)

    # Save tasks to file
    def save_tasks(self):
        self.file_handler.save_tasks(self.tasks, self.filename)
        print("Tasks saved successfully!")

    # Load tasks from file
    def load_tasks(self):
        self.tasks = self.file_handler.load_tasks(self.filename)
        print("Tasks loaded successfully!")

    # Menu
    def menu(self):
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                tid = input("Enter Task ID: ").strip()
                title = input("Enter Title: ").strip()
                desc = input("Enter Description: ").strip()
                due = input("Enter Due Date (YYYY-MM-DD, optional): ").strip()
                status = input("Enter Status (Pending/In Progress/Completed): ").strip()
                self.add_task(Task(tid, title, desc, due, status))
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                tid = input("Enter Task ID to update: ").strip()
                title = input("Enter new Title (leave blank to skip): ").strip() or None
                desc = input("Enter new Description (leave blank to skip): ").strip() or None
                due = input("Enter new Due Date (leave blank to skip): ").strip() or None
                status = input("Enter new Status (leave blank to skip): ").strip() or None
                self.update_task(tid, title, desc, due, status)
            elif choice == "4":
                tid = input("Enter Task ID to delete: ").strip()
                self.delete_task(tid)
            elif choice == "5":
                status = input("Enter status to filter: ").strip()
                self.filter_tasks(status)
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                self.load_tasks()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


# ---------------- Main ----------------
if __name__ == "__main__":
    file_handler = CSVTaskFileHandler()
    manager = TaskManager(file_handler, "tasks.csv")
    manager.menu()