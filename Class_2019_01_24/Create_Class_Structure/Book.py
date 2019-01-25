from .Document import Document
from datetime import datetime

class Book(Document):

    def __init__(self, input_title, input_authors: str, input_day: int, input_month: int, input_year:int):

        self.__title = input_title
        super().__init__(input_authors: str, input_day: int, input_month: int, input_year:int)

    def get_title(self):
        """Return subject"""
        return self.__title