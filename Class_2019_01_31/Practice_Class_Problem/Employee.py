from Worker import Worker


class Employee(Worker):
    def init__(self, input_yearly_salary, input_id, input_name, hire_date):
        self.__yearly_salary = input_yearly_salary
        super().__init__(input_id, input_name, hire_date)


    def set_yearly_salary(self, new_yearly_salary):
        self.__yearly_salary = new_yearly_salary
        return self.__yearly_salary


    def get_yearly_salary(self):
        return self.__yearly_salary


    def get_hourly_salary(self):
        working_days = 261
        hours_per_day = 8
        self.__hourly_salary = self.__yearly_salary/(working_days*hours_per_day)
        return self.__hourly_salary


test_emp01 = Employee(35000,32145,"John")
print(test_emp01.get_name())
print(test_emp01.get_yearly_salary())