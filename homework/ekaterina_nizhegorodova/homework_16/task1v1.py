import mysql.connector as mysql
import dotenv
import os
import csv


# open csv file and get data as a list of dicts
base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(base_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")
print(file_path)
with open(file_path, newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)

# connect to db and get data as a list of dicts
dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)
query_info = '''
select s.name, s.second_name, g.title as group_title, b.title as book_title,
s2.title as subject_title, l.title as lesson_title, m.value as mark_value
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
'''
cursor.execute(query_info)
data_info = cursor.fetchall()

# compare dicts
for row in data:
    if row in data_info:
        pass
    else:
        print(row)

db.close()
