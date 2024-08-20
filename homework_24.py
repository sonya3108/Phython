import sqlite3


DB_PATH = 'our_db_13052024.sqlite3'


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


cursor.execute('''
DROP TABLE IF EXISTS Schools
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Schools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    school_number INTEGER NOT NULL,        
    address TEXT NOT NULL,                 
    number_of_floors INTEGER NOT NULL CHECK (number_of_floors >= 1)  
)
''')


cursor.execute('''
DROP TABLE IF EXISTS Students
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    last_name TEXT NOT NULL,               
    first_name TEXT NOT NULL,              
    specialization TEXT,                   
    school_id INTEGER,                     
    phone_number TEXT,                     
    FOREIGN KEY (school_id) REFERENCES Schools(id)  
)
''')


conn.commit()


schools = [
    (1, 'Shevchenko Street, 10', 3),
    (2, 'Hrushevsky Street, 5', 2),
    (3, 'Franko Street, 20', 4)
]
cursor.executemany('''
INSERT INTO Schools (school_number, address, number_of_floors)
VALUES (?, ?, ?)
''', schools)


students = [
    ('Ivanov', 'Ivan', 'Math', 1),
    ('Petrov', 'Petr', 'Physics', 1),
    ('Sidorov', 'Sidor', 'Biology', 2),
    ('Kuznetsov', 'Nikolay', 'History', 3),
    ('Smirnov', 'Alexey', 'Chemistry', 1),
    ('Volkov', 'Dmitry', 'Math', 2),
    ('Sergeev', 'Sergey', 'Geography', 3),
    ('Ivanova', 'Anna', 'Math', 1),
    ('Petrova', 'Olga', 'Physics', 3),
    ('Sidorova', 'Elena', 'Biology', 2)
]
cursor.executemany('''
INSERT INTO Students (last_name, first_name, specialization, school_id)
VALUES (?, ?, ?, ?)
''', students)


conn.commit()


cursor.execute('''
SELECT Students.id, Students.last_name, Students.first_name, Students.specialization, Schools.school_number, Schools.address 
FROM Students
LEFT JOIN Schools ON Students.school_id = Schools.id
''')
students_with_schools = cursor.fetchall()
print("Список всіх учнів з інформацією про школи:")
for student in students_with_schools:
    print(student)


cursor.execute('''
UPDATE Students
SET phone_number = ?
WHERE id = ?
''', ('38099659418', 5))


conn.commit()


cursor.execute('''
DELETE FROM Students
WHERE id BETWEEN 2 AND 4
''')


conn.commit()


cursor.execute('''
SELECT id, last_name, first_name, phone_number 
FROM Students
ORDER BY id DESC
LIMIT 3 OFFSET 2
''')
last_students = cursor.fetchall()
print("\nТри передостанні учні (пропускаючи перших двох):")
for student in last_students:
    print(student)


conn.close()

print(f"Database operations completed. Database path: {DB_PATH}")






