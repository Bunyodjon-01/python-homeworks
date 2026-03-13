from datetime import datetime

current_year = datetime.now().year

name = input("your name: ")
birth_year = int(input("your birth year: ")) 
age = current_year - birth_year

print(f"{name} is {age} years old")