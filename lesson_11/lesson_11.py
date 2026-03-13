## Task 1
import sqlite3

connection = sqlite3.connect("roster.db")
create_table = '''
    create table if not exists "Roster" (
        name nvarchar(100),
        species nvarchar(100),
        age int
        );
'''
values = '''
    insert into Roster
    values
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29);
'''
cursor = connection.cursor()
cursor.execute(create_table)
cursor.execute(values)
connection.commit()
connection.close()

import sqlite3

connection = sqlite3.connect("roster.db")

query = '''
    UPDATE Roster
    SET name = 'Ezri Dax'
    WHERE name = 'Jadzia Dax';
'''
cursor = connection.cursor()
cursor.execute(query)
connection.commit()
connection.close()


import sqlite3

connection = sqlite3.connect("roster.db")

query = '''
    select name, age from roster
    where species = "Bajoran"
'''
cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchall()
for i in results:
    print(i)
connection.close()

import sqlite3

connection = sqlite3.connect("roster.db")

query = '''
    DELETE from roster
    where age > 100;
'''
cursor = connection.cursor()
cursor.execute(query)
connection.commit()
connection.close()


import sqlite3

connection = sqlite3.connect("roster.db")

query = '''
    select * from roster
    order by age desc;
'''
cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchall()
for i in results:
    print(i)
connection.close()



##############Task 2
import sqlite3

connection = sqlite3.connect("library.db")
create_table = '''
    create table if not exists Books (
        Title nvarchar(100),
        Author nvarchar(100),
        Year_Published int,
        Genre nvarchar(100)
        );
'''
values = '''
    insert into Books
    values
        ("To Kill a Mockingbird", "Harper Lee ", 1960, "Fiction"),
        ("1984", "George Orwell ", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic");
'''
cursor = connection.cursor()
cursor.execute(create_table)
cursor.execute(values)
connection.commit()
connection.close()

import sqlite3

connection = sqlite3.connect("library.db")

query = '''
    UPDATE Books
    SET Year_Published = 1950
    WHERE Title = '1984';
'''
cursor = connection.cursor()
cursor.execute(query)
connection.commit()
connection.close()


import sqlite3

connection = sqlite3.connect("library.db")

query = '''
    select Title, Author from Books
    where Genre = "Dystopian"
'''
cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchall()
for i in results:
    print(i)
connection.close()

import sqlite3

connection = sqlite3.connect("library.db")

query = '''
    DELETE from Books
    where Year_Published < 1950;
'''
cursor = connection.cursor()
cursor.execute(query)
connection.commit()
connection.close()


import sqlite3

connection = sqlite3.connect("library.db")

query = '''
    select * from Books
    order by Year_Published asc;
'''
cursor = connection.cursor()
cursor.execute(query)
results = cursor.fetchall()
for i in results:
    print(i)
connection.close()
