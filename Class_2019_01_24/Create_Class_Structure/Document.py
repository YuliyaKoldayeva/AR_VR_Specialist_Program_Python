from datetime import datetime

class Document:

    def __init__(self, input_authors: str, input_day: int, input_month: int, input_year:int):
        """Instantiate a new Document object"""
        self.__authors = input_authors.title()

        try:
            # create data string with the inputs from user
            date_string = '{}/{}/{}'.format(input_year, input_month, input_day)
            # transform date_string into date format
            self.__doc_date = (datetime.strptime(date_string, '%Y/%m/%d')).date()

        except:   # catches abnormal values
            print("\n\nERROR MESSAGE FOR THE WRONG DATE INPUT:"
                  "\n\nThe format for the date should be:"
                  "\n\tdigits from 1 to 31 for the day "
                  "\n\tdigits from 1 to 12 for the month"
                  "\n\tfour digits for year."
                  "\n\nPlease, try again.\n")


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
# my_doc2 = Document("Another Author", 30, 13, 1956)
# my_doc3 = Document("Another Author", 35, 10, 1756)
# my_doc4 = Document("Another Author", 3, 1, 56)