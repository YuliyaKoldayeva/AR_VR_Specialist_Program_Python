from random import randint

class PyCalc():
    """Class which acts as a calculator."""

    def __init__(self, my_list):
        """Instantiate a new object"""
        self.__my_list = my_list

    def get_average(self):
        """Calculate the average of the list manually."""
        return sum(self.__my_list)/len(self.__my_list)

    def get_min_value(self):
        """Calculate the minimum value of the list."""
        list_to_sort = (self.__my_list).copy() # to avoid any modification to the original list
        list_to_sort.sort()
        return list_to_sort[0]

    def get_max_value(self):
        """Calculate the maximum value of the list."""
        list_to_sort = (self.__my_list).copy() # to avoid any modification to the original list
        list_to_sort.sort()
        return list_to_sort[-1]

    def set_clear(self):
        """Clear the list in the class => Empty list"""
        self.__my_list = []
        return "OK"

    def generate_random_data(self, elements_number, from_number, up_to_number):
        """Generate the desired number of random numbers in the desired interval"""
        for element in range(elements_number):
            (self.__my_list).append(randint(from_number, up_to_number))
        return self.__my_list


print("\n\tPRINTING HARD CODDED EXAMPLE\n")
my_list = [110, 15, 20, 55]
print("Here is my list of numbers: {}".format( my_list))

c = PyCalc(my_list)
print("\nThe average value of this list of numbers is is:", c.get_average())
print("\nMin value is:", c.get_min_value())
print("\nMax value is:", c.get_max_value())

print("\n\n\tPRINTING COMPUTER GENERATED EXAMPLES\n")

print("\nThe new list is:", c.generate_random_data(5,0,1))
print("\nClear the list:", c.set_clear())
print("\nThe new list is:", c.generate_random_data(15,0,100))
print("\nMin value is:", c.get_min_value())
print("\nMax value is:", c.get_max_value())
