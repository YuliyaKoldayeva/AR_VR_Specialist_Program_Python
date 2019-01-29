from Document import Document

class Email(Document):

    def __init__(self, input_subject: str, input_to_whom: list, input_authors: list,
                 input_day: int, input_month: int, input_year: int):
        """Instantiate a new Email object"""
        self.__subject = input_subject.title()
        self.__to = input_to_whom
        super().__init__(input_authors, input_day, input_month, input_year)

    def get_subject(self):
        """Return subject"""
        return self.__subject

    def get_to(self):
        """Return subject"""
        return self.__to


# TESTING AREA
email_object = Email("does it work?", ["yuliya"], ["myself"], 25, 1, 2019)

print("\nE-mail subject is:", email_object.get_subject())
print("\nE-mail was sent to:", email_object.get_to())
print("\nE-mail sender is:", email_object.get_authors())
print("\nE-mail was send on:", email_object.get_date())


