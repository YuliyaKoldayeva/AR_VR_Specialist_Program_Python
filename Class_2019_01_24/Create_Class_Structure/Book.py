from Document import Document


class Book(Document):
    def __init__(self, input_title, input_authors: str, input_day: int, input_month: int, input_year:int):
        """Instantiate a new Book object"""
        self.__title = input_title
        super().__init__(input_authors, input_day, input_month, input_year)

    def get_title(self):
        """Return subject"""
        return self.__title

#"Testing area"


book1 = Book("Any Title", "Some Author", 25, 10, 2015)

print("\nBook Title is:",book1.get_title())
print("\nBook Author is:",book1.get_authors())
print("\nBook was published on:", book1.get_date())