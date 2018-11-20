import random
students_number = input("How many students are in the class (please type here) : ")
students_number_numeric = int(students_number)
students_list = []
for number in range(1,students_number_numeric+1):
    students_list.append(number)

print(students_list)
input("Press enter to chose the first student ")
for number in range(students_number_numeric-1):
    stop_value = students_number_numeric - number
    random_student = random.randint(1,stop_value-1)
    print(students_list.pop(random_student))
    input("Press enter to chose the next student ")
print(students_list.pop())