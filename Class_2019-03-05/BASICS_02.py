

def create_list(min_value, max_value):

    list_of_numbers = list(range(min_value, max_value+1))

    return list_of_numbers


def check_if_prime(element):

    number_is_prime = True

    if element != 1:

        for each in range(2, element):
            if element%each == 0:
                return False


print("My list is", create_list(1,100))



