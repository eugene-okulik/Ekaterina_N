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

# connect to db
dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

# specify query
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
WHERE s.name = %s AND s.second_name = %s
AND g.title = %s AND b.title = %s
AND s2.title = %s AND l.title = %s AND m.value = %s
'''

# check each raw from csv in db, getting only values from dict as a tuple
for x in data:  # type: dict
    data_for_query = tuple(x.values())
    cursor.execute(query_info, data_for_query)
    result = cursor.fetchall()
    if not result:
        print(f' Data has not been found in db: {x}')

db.close()
