class Worker:

    def __init__(self, input_id, input_name, hire_date):

        self.__id = input_id
        self.__name = input_name
        self.__hire_date = hire_date


    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name


    def get_hire_date(self):
        return self.__hire_date

    def set_hire_date(self, new_hire_date):
        self.__hire_date = new_hire_date


# test_worker=Worker(12354, "Erik", "Dec 14, 2011")
# print(test_worker.get_name())
# print(test_worker.get_id())
# print(test_worker.get_hire_date())