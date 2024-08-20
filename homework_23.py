import sqlite3


DB_PATH = 'our_db_13052024.sqlite3'


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS schools (
        school_id INTEGER PRIMARY KEY AUTOINCREMENT,
        school_number INTEGER NOT NULL,
        address TEXT NOT NULL,
        floors INTEGER NOT NULL CHECK(floors >= 1)
    )
''')


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name TEXT NOT NULL,
        first_name TEXT NOT NULL,
        specialization TEXT,
        school_id INTEGER,
        FOREIGN KEY (school_id) REFERENCES schools (school_id)
    )
''')


cursor.execute('''
    INSERT INTO schools (school_number, address, floors)
    VALUES (?, ?, ?)
''', (1, '123 Main St', 3))

cursor.execute('''
    INSERT INTO schools (school_number, address, floors)
    VALUES (?, ?, ?)
''', (2, '456 Elm St', 2))

cursor.execute('''
    INSERT INTO schools (school_number, address, floors)
    VALUES (?, ?, ?)
''', (3, '789 Oak St', 4))


students = [
    ('Ivanov', 'Ivan', 'Math', 1),
    ('Petrov', 'Petr', 'Physics', 1),
    ('Sidorov', 'Sidr', 'Chemistry', 1),
    ('Smirnov', 'Nikolai', 'Math', 2),
    ('Kuznetsov', 'Alexey', 'Physics', 2),
    ('Popov', 'Sergey', 'Biology', 2),
    ('Vasiliev', 'Vasiliy', 'History', 3),
    ('Pavlov', 'Pavel', 'Literature', 3),
    ('Semenov', 'Semen', 'Geography', 3),
    ('Fedorov', 'Fedor', 'English', 3)
]

cursor.executemany('''
    INSERT INTO students (last_name, first_name, specialization, school_id)
    VALUES (?, ?, ?, ?)
''', students)

conn.commit()


cursor.execute('''
    SELECT students.student_id, students.last_name, students.first_name, students.specialization, schools.school_number, schools.address
    FROM students
    JOIN schools ON students.school_id = schools.school_id
''')

students = cursor.fetchall()

for student in students:
    print(student)


conn.close()





