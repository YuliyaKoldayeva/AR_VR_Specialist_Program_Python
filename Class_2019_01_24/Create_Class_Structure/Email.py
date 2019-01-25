from .Document import Document
from datetime import datetime

class Email(Document):

    def __init__(self, input_subject, input_to_whom, input_authors: str, input_day: int, input_month: int, input_year:int):

        self.__subject = input_subject
        self.__to = input_to_whom
        super().__init__(input_authors: str, input_day: int, input_month: int, input_year:int)

    def get_subject(self):
        """Return subject"""
        return self.__subject

    def get_to(self):
        """Return subject"""
        return self.__to

