class BookNotFoundException(Exception): pass
class BookAlreadyBorrowedException(Exception): pass
class MemberLimitExceededException(Exception): pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        self.limit = 3

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.title] = book

    def add_member(self, member):
        self.members[member.name] = member

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException(f"Kitob topilmadi: {book_title}")
        
        book = self.books[book_title]
        member = self.members.get(member_name)

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"'{book_title}' allaqachon ijaraga olingan.")
        
        if len(member.borrowed_books) >= member.limit:
            raise MemberLimitExceededException(f"{member_name} 3 tadan ortiq kitob ololmaydi.")

        book.is_borrowed = True
        member.borrowed_books.append(book_title)
        print(f"{member_name} '{book_title}' kitobini oldi.")

    def return_book(self, member_name, book_title):
        if book_title in self.books:
            self.books[book_title].is_borrowed = False
            self.members[member_name].borrowed_books.remove(book_title)
            print(f"{member_name} '{book_title}' kitobini qaytardi.")

# Test qilish
lib = Library()
lib.add_book(Book("O'tkan Kunlar", "Abdulla Qodiriy"))
lib.add_book(Book("Python Asoslari", "Guido Van Rossum"))
lib.add_member(Member("Ali"))

try:
    lib.borrow_book("Ali", "O'tkan Kunlar")
    lib.borrow_book("Ali", "O'tkan Kunlar") # Xatolik: Allaqachon olingan
except Exception as e:
    print(f"Xato: {e}")

############################################################################

import csv

# 1. grades.csv faylini yaratish
data = [
    ['Name', 'Subject', 'Grade'],
    ['Alice', 'Math', 85],
    ['Bob', 'Science', 78],
    ['Carol', 'Math', 92],
    ['Dave', 'History', 74]
]

with open('grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# 2. O'qish va hisoblash
subjects = {}
with open('grades.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        sub = row['Subject']
        grade = int(row['Grade'])
        if sub not in subjects:
            subjects[sub] = []
        subjects[sub].append(grade)

# 3. average_grades.csv fayliga yozish
with open('average_grades.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Subject', 'Average Grade'])
    for sub, grades in subjects.items():
        avg = sum(grades) / len(grades)
        writer.writerow([sub, avg])

print("O'rtacha ballar 'average_grades.csv' fayliga saqlandi.")
####################################################################


import json
import csv

# 1. JSON fayl yaratish
tasks_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

with open('tasks.json', 'w') as f:
    json.dump(tasks_data, f, indent=4)

def manage_tasks():
    # Yuklash
    with open('tasks.json', 'r') as f:
        tasks = json.load(f)

    # Ko'rsatish
    print(f"{'ID':<5} {'Task':<20} {'Status':<12} {'Priority'}")
    for t in tasks:
        status = "Done" if t['completed'] else "Pending"
        print(f"{t['id']:<5} {t['task']:<20} {status:<12} {t['priority']}")

    # Statistika
    total = len(tasks)
    completed = sum(1 for t in tasks if t['completed'])
    avg_priority = sum(t['priority'] for t in tasks) / total
    
    print(f"\nStats: Total: {total}, Completed: {completed}, Pending: {total-completed}, Avg Priority: {avg_priority:.2f}")

    # CSV ga o'tkazish
    with open('tasks.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "task", "completed", "priority"])
        writer.writeheader()
        writer.writerows(tasks)

manage_tasks()


##########################################################################################