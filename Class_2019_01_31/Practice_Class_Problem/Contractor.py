from Worker import Worker


class Contractor(Worker):

    def init__(self, input_hourly_salary, input_id, input_name, hire_date):
        self.__input_hourly_salary = input_hourly_salary
        super.__init__(input_id, input_name, hire_date)


    def set_hourly_salary(self, new_hourly_salary):
        self.__hourly_salary = new_hourly_salary
        return self.__hourly_salary


    def get_hourly_salary(self):
        return self.__hourly_salary


test_emp01 = Contractor(35000,32145,"John","2001 Jan 23")
print(test_emp01.get_name)