import re


def is_numeric(test_string):
    pattern = '^[0-9]+$'
    return re.match(pattern, test_string)


def is_character(test_string):
    pattern = '^[a-zA-Z]{1}$'
    return re.match(pattern, test_string)


def is_special_character(test_string):
    pattern = '^[\!\@\#\$\%\^\&\*\(\)]{1}$'
    return re.match(pattern, test_string)

def is_even_number(element):
    if element%2==0:
        return "This is an even number. "
    else:
        return ""


def numeric_list_max(input_list):
    only_numbers = []
    for element in input_list:
        test_string = str(element)
        if is_numeric(test_string):
            only_numbers.append(element)
    return max(only_numbers)


def current_vs_max(input_list, element):
    if numeric_list_max(input_list) == element:
        return "This is the highest number in the list."
    else:
        return "This is NOT the highest number in the list."



def go_through_the_list(input_list):
    counter = 0
    character_set=set()
    for element in input_list:
        counter +=1
        test_string = str(element)
        print("Element #{}: Value is {}. ".format(counter, element), end="")

        if is_numeric(test_string):
            print("This is a number. " + is_even_number(element) + current_vs_max(input_list, element))

        elif is_character(test_string):
            character_set.add(test_string)
            print("This is a character. So far, the characters found are", sorted(character_set))

        elif is_special_character(test_string):
            print("This is a special character")

        else:
            print("This is an element without clear classification")



input_list = [6, "g", 5, "b", "$", "c", 7, 26, 5, "z", "!", "p6"]

go_through_the_list(input_list)

