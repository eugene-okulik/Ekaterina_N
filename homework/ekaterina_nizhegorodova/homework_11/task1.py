class Book:
    material = "бумага"
    has_text = True

    def __init__(self, name, author, page_total, isbn, is_reserved):
        self.name = name
        self.author = author
        self.page_total = page_total
        self.isbn = isbn
        self.is_reserved = bool(is_reserved)

    def show_info(self):
        if self.is_reserved is True:
            self.is_reserved = "зарезервирована"
            print(f"Название: {self.name}, Автор: {self.author}, "
                  f"страниц: {self.page_total}, материал: {self.material}, {self.is_reserved}")
        else:
            print(f"Название: {self.name}, Автор: {self.author}, страниц: {self.page_total}, "
                  f"материал: {self.material}")


class SchoolTutorial(Book):
    def __init__(self, name, author, page_total, isbn, is_reserved, subject, grade, has_tasks):
        super().__init__(name, author, page_total, isbn, is_reserved)
        self.subject = subject
        self.grade = grade
        self.has_tasks = bool(has_tasks)

    def show_info(self):
        if self.is_reserved is True:
            self.is_reserved = "зарезервирована"
            print(f"Название: {self.name}, Автор: {self.author}, страниц: {self.page_total}, "
                  f"предмет: {self.subject}, класс: {self.grade}, {self.is_reserved}")
        else:
            print(f"Название: {self.name}, Автор: {self.author}, страниц: {self.page_total}, "
                  f"предмет: {self.subject}, класс: {self.grade}")


book1 = Book("Идиот", "Ф. М. Достоевский", 640, "978-5-389-04730-3", False)
book2 = Book("Контакт", "К. Саган", 515, "978-5-00139-428-0", False)
book3 = Book("Гиперион. Падение Гипериона", "Д. Симмонс", 976,
             "978-5-17-085290-1", False)
book4 = Book("Эндимион. Восход Эндимиона", "Д. Симмонс", 976,
             "978-5-17-085322-9", False)
book5 = Book("Последняя война", "К. Булычёв", 928, "978-5-389-23330-0", False)
book2.is_reserved = True
book1.show_info()
book2.show_info()
book3.show_info()
book4.show_info()
book5.show_info()
tutorial1 = SchoolTutorial("География. Физическая география", "Е. Кольмакова", 184,
                           "978-985-03-3814-3", False, "География", 6, False)
tutorial2 = SchoolTutorial("Физика", "В. Жилко", 287, "978-985-03-3623-1",
                           False, "Физика", 11, True)
tutorial3 = SchoolTutorial("Химия", "И. Борушко", 304, "978-985-599-299-9",
                           False, "Химия", 11, True)
tutorial2.is_reserved = True
tutorial1.show_info()
tutorial2.show_info()
tutorial3.show_info()
