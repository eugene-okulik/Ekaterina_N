import mysql.connector as mysql

db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl"
)

cursor = db.cursor(dictionary=True)

# Insert student
insert_student = "INSERT into students (name, second_name, group_id) values (%s, %s, NULL)"
cursor.execute(insert_student, ('Korben', 'Dallas'))
student_id = cursor.lastrowid

# Insert books
insert_books = "INSERT into books (title, taken_by_student_id) values (%s, %s)"
cursor.executemany(
    insert_books, [
        ('Diva Plavalaguna songs lyrics', student_id),
        ('Multipass validation tutorial', student_id),
        ('How to fix flying taxi vehicle', student_id)
    ]
)

# Create group
insert_group = "INSERT INTO `groups` (title, start_date, end_date) values (%s, %s, %s)"
cursor.execute(insert_group, ('World saver', 'sep 2022', 'oct 2025'))
group_id = cursor.lastrowid

# Assign student to group
update_group = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(update_group, (group_id, student_id))

# Create subjects
insert_subjects = "INSERT into subjets (title) values (%s)"
cursor.executemany(insert_subjects, [('How to be a hero',), ('Taxi driving',), ('Fighting',)])
subject_ids = [cursor.lastrowid, cursor.lastrowid, cursor.lastrowid]

# Create lessons
insert_lessons = "INSERT INTO lessons (title, subject_id) values (%s, %s)"
cursor.executemany(
    insert_lessons, [
        ('How to be brave as hell', subject_ids[0]),
        ('How to smile like a hero', subject_ids[0]),
        ('Traffic in the air', subject_ids[1]),
        ('Catch up passengers in the air', subject_ids[1]),
        ('Fight like a Bruce Willis', subject_ids[2]),
        ('Aikido', subject_ids[2])
    ]
)
lesson_ids = [cursor.lastrowid, cursor.lastrowid, cursor.lastrowid,
              cursor.lastrowid, cursor.lastrowid, cursor.lastrowid]

insert_marks = "INSERT INTO marks (value, lesson_id, student_id) values (%s, %s, %s)"
cursor.executemany(
    insert_marks, [
        ('9', lesson_ids[0], student_id),
        ('10', lesson_ids[1], student_id),
        ('3', lesson_ids[2], student_id),
        ('4', lesson_ids[3], student_id),
        ('10', lesson_ids[4], student_id),
        ('8', lesson_ids[5], student_id)
    ]
)

db.commit()

query_all_marks = '''
SELECT m.value, l.title from marks m
join lessons l on l.id = m.lesson_id
WHERE student_id = %s
'''
cursor.execute(query_all_marks, (student_id,))
data_marks = cursor.fetchall()
print(f"All student's marks: {data_marks}")

query_all_books = "SELECT title from books WHERE taken_by_student_id = %s"
cursor.execute(query_all_books, (student_id,))
data_books = cursor.fetchall()
print(f"Student's books: {data_books}")

query_all_info = '''
select s.name, s.second_name, g.title as group_title, g.start_date, g.end_date,
b.title as book_title, s2.title as subject, l.title as lesson, m.value
FROM students s
JOIN `groups` g
on g.id = s.group_id
JOIN books b
on b.taken_by_student_id = s.id
JOIN marks m
on m.student_id = s.id
JOIN lessons l
on l.id = m.lesson_id
JOIN subjets s2
on s2.id = l.subject_id
WHERE s.id = %s
'''
cursor.execute(query_all_info, (student_id,))
data_info = cursor.fetchall()
print(f"Student's all info: {data_info}")

db.close()
