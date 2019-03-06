input_list_a = [3,6,2,1,5,66,2,22]
input_list_b = input_list_a.copy()

def find_min_value(input_list_b):
    min_value = input_list_b[0]
    for each in input_list_b:
        if each < min_value:
            min_value = each
    return min_value

print(find_min_value(input_list_b))


def reordering_list(input_list_b):
    new_list =[]
    for number in range(len(input_list_b)):
        new_element = find_min_value(input_list_b)
        new_list.append(new_element)
        input_list_b.remove(find_min_value(input_list_b))
    return new_list


def display_result(input_list_a):
    print("Size = {}".format(len(input_list_b)))
    print("Content \n {}".format(reordering_list(input_list_b)))

display_result(input_list_b)


