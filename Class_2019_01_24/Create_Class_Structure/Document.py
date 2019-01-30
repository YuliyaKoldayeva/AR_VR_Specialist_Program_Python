from datetime import datetime

class Document:

    def __init__(self, input_authors: list, input_day: int, input_month: int, input_year: int):
        """Instantiate a new Document object"""
        self.__authors = input_authors

        try:
            # create data string with the inputs from user
            date_string = '{}/{}/{}'.format(input_year, input_month, input_day)
            # transform date_string into date format
            self.__doc_date = (datetime.strptime(date_string, '%Y/%m/%d')).date()

        except:   # catches abnormal values
            print("\n\nERROR MESSAGE FOR THE WRONG DATE INPUT:"
                  "\n\nThe format for the date should be:"
                  "\n\tnumbers from 1 to 31 for the day "
                  "\n\tnumbers from 1 to 12 for the month"
                  "\n\tfour digits for year."
                  "\n\nPlease, try again.\n")


    def get_authors(self):
        """Return Authors"""
        return self.__authors

    def get_date(self):
        """Return Date"""
        return self.__doc_date

    def add_author(self, new_author_name: str):
        """Add Author"""
        (self.__authors).append(new_author_name)


#TESTING AREA

# authors_list = ["Some Author"]
# my_doc = Document(authors_list, 5, 3, 1956)
# print(my_doc.get_authors())
# print("\nDate is:", my_doc.get_date())
# print("\nAuthor field:", my_doc.get_authors())
# my_doc5 = Document(["The Only Author"], 5, 3, 1956)
# my_doc5.add_author("New Author")
# print("\nAuthor field:", my_doc5.get_authors())
# my_doc6 = Document(["First Author"], 5, 3, 1956)
# my_doc6.add_author("Additional Author")
# print("\nAuthor field:", my_doc6.get_authors())
