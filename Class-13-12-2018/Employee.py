class Worker:

    def __init__(self, worker_name = ""):
        self.__name = worker_name

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name


class Employee(Worker):

    def __init__(self, initial_salary):
        self.salary = initial_salary

    def set_salary(self, new_salary):
        self.salary = new_salary