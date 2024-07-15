Создайте студента (student):
INSERT into students (name, second_name, group_id) values ('Phoebe', 'Buffay', '129')

Создайте несколько книг (books) и укажите, что ваш созданный студент взял их:
INSERT into books (title, taken_by_student_id)
values ('Minsk - guide-book', '1427'),
('Meditation', '1427'),
('Evolution theory', '1427')

Создайте группу (group) и определите своего студента туда:
Create group:
INSERT INTO `groups` (title, start_date, end_date) values ('Friends', 'sep 2022', 'oct 2025')
UPDATE students SET group_id = '1412' WHERE id = '1427'

Создайте несколько учебных предметов (subjects)
INSERT into subjets (title) values ('Gitar'), ('Taro'), ('Indian philosophy')

Создайте по два занятия для каждого предмета (lessons):
INSERT INTO lessons (title, subject_id)
values ('Gitar for begginers', '1889'),
('Introdaction to Taro', '1890'),
('Karma for beginners', '1891'),
('Introdaction to Taro p.2', '1890'),
('Karma for beginners p.2', '1891'),
('Gitar for begginers p.2')

Поставьте своему студенту оценки (marks) для всех созданных вами занятий:
INSERT INTO marks (value, lesson_id, student_id)
values ('6', '4278', '1427'),
('8', '4279', '1427'),
('10', '4280', '1427'),
('10', '4281', '1427'),
('9', '4282', '1427'),
('7', '4283', '1427')

Все оценки студента:
SELECT m.value, l.title from marks m
join lessons l on l.id = m.lesson_id
WHERE student_id = '1427'

Все книги, которые находятся у студента:
SELECT title from books WHERE taken_by_student_id = '1427'

Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов (всё одним запросом с использованием Join):
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
WHERE s.id = '1427'

