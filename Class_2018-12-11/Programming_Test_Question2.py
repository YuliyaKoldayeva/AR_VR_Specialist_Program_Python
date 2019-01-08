# Creating a list

def ask_user():
    return input('Please enter an element to add to the list (or type "fin" to finish) >> ')


my_list = [] # initializing the list to save user's inputs
user_element = ask_user()

# Check if user wants to finish or to add a new element
while user_element != "fin":
    my_list.append(user_element.title())

    # ask for a new entry
    user_element = ask_user()

# Print the final result
print("The list contain {} elements, here they are: ".format(len(my_list)))

for number in range(0,len(my_list)):
    print("{}: {}".format(number+1, my_list[number]))

