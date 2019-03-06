def create_list(min_value, max_value):
    list_of_numbers = list(range(min_value, max_value+1))
    return list_of_numbers


def check_if_prime(element):

    if element > 2:
        for each in range(2, element):
            if (element%each) == 0:
                return "This is NOT a prime number"
        return "This is a PRIME NUMBER"
    elif element == 2:
        return "This is a prime number"
    elif element == 1:
        return "This is NOT a prime number"


def check_the_elements(my_list):
    for each in my_list:
        print(each, check_if_prime(each))


my_list = create_list(1,100)
print("Creating my list of numbers from 1 to 100", my_list)

check_the_elements(my_list)




