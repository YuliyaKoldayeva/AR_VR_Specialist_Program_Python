
import random

# Create an empty list.
my_list = []
contains_value = False

for x in range(10):

    while True:

        rand_val = random.randint(1, 10)

        contains_value = False

        # Check if new random value exists in the current list.
        for v in my_list:
            if v == rand_val:
                contains_value = True

        # If not existing, add it and break out of the loop.
        if not contains_value:
            my_list.append(rand_val)
            break

print(my_list)





"""

import random
students_number = input("How many students are in the class (please type here) : ")
students_number_numeric = int(students_number)
students_list = []
for number in range(1,students_number_numeric+1):
    students_list.append(number)

input("Press enter to chose the first student ")
for number in range(students_number_numeric-1):
    stop_value = students_number_numeric - number
    random_student = random.randint(0,stop_value-1)
    print(students_list.pop(random_student))
    input("Press enter to chose the next student ")
print(students_list.pop())
print("It was the last student remained")
"""