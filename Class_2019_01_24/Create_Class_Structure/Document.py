from datetime import datetime

class Document:

    def __init__(self, input_authors: str, input_day: int, input_month: int, input_year:int):
        """Instantiate Document object
        type two digits for day and month , i.g.: Mars => 03, day 5 => 05
        type four digits for year, i.g.: 1987 """

        self.__authors = input_authors
        date_string = '{}/{}/{}'.format(input_year, input_month, input_day) # create data string with the inputs from user
        self.__doc_date = (datetime.strptime(date_string, '%Y/%m/%d')).date() # transform date_string into date format

    def get_authors(self):
        """Return Authors"""
        return self.__authors

    def get_date(self):
        """Return Date"""
        return self.__doc_date

    def add_author(self, author_name: str):
        """Set Author"""
        self.__authors = author_name


# TESTING AREA
# my_doc = Document("Some Author", 5, 3, 1956)
# print("Date is:", my_doc.get_date())
# print("Author is:", my_doc.get_authors())