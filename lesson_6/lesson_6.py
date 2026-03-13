### Zero Check Decorator
def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper


@check
def div(a, b):
    return a / b


print(div(6, 2))
print(div(6, 0))


### **Employee Records Manager**

FILE = "employees.txt"


def add_employee():
    with open(FILE, "a") as f:
        emp = input("Enter ID, Name, Position, Salary: ")
        f.write(emp + "\n")


def view_all():
    with open(FILE, "r") as f:
        print(f.read())


def search_employee(emp_id):
    with open(FILE, "r") as f:
        for line in f:
            if line.startswith(emp_id + ","):
                print(line)
                return
    print("Employee not found")


def update_employee(emp_id):
    updated = []
    found = False
    with open(FILE, "r") as f:
        for line in f:
            if line.startswith(emp_id + ","):
                new_data = input("Enter new ID, Name, Position, Salary: ")
                updated.append(new_data + "\n")
                found = True
            else:
                updated.append(line)

    if found:
        with open(FILE, "w") as f:
            f.writelines(updated)
    else:
        print("Employee not found")


def delete_employee(emp_id):
    lines = []
    with open(FILE, "r") as f:
        for line in f:
            if not line.startswith(emp_id + ","):
                lines.append(line)

    with open(FILE, "w") as f:
        f.writelines(lines)


while True:
    print("""
1. Add
2. View
3. Search
4. Update
5. Delete
6. Exit
""")
    choice = input("Choose: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_all()
    elif choice == "3":
        search_employee(input("Employee ID: "))
    elif choice == "4":
        update_employee(input("Employee ID: "))
    elif choice == "5":
        delete_employee(input("Employee ID: "))
    elif choice == "6":
        break

### **Word Frequency Counter**

import os
import string
from collections import Counter

FILE = "sample.txt"
REPORT = "word_count_report.txt"

if not os.path.exists(FILE):
    text = input("Enter text for sample.txt:\n")
    with open(FILE, "w") as f:
        f.write(text)

with open(FILE, "r") as f:
    text = f.read().lower()

text = text.translate(str.maketrans("", "", string.punctuation))
words = text.split()

counter = Counter(words)
total_words = len(words)

top_n = int(input("How many top words to show? "))
top_words = counter.most_common(top_n)

print(f"Total words: {total_words}")
for word, count in top_words:
    print(f"{word} - {count}")

with open(REPORT, "w") as f:
    f.write("Word Count Report\n")
    f.write(f"Total Words: {total_words}\n")
    f.write("Top Words:\n")
    for word, count in top_words:
        f.write(f"{word} - {count}\n")
