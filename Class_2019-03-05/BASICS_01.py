import re

input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!"]


def check_if_number(element):

    if re.match("^[0-9]+$", element):
        return True
    else:
        return False



print(check_if_number(5))
print(check_if_number("a"))

"""


def find_max_value(input_list):
    list_of_numbers = []
    for element in input_list:
        if check_if_number(element):
            list_of_numbers.append(element)

    return max(list_of_numbers)



def print_the_statement(element,index):

    statement = ("Element #{}".format(index))

    return statement




def go_through_the_list(input_list):

    for element in input_list:
        check_if_number(element)




print(go_through_the_list(input_list))
"""