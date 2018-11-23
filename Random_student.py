import random
list=[]
student_num = input("Please, type the number of students in this class: >>>  ")
print("The sequence of random numbers is as follows: ")
student_num_int = int(student_num)
for number in range(1,student_num_int+1):
    list.append(number)

for number in range(1,student_num_int+1):
    up_to = (student_num_int-number)

    index = random.randint(0,up_to)

    print("number", list.pop(index))
    if up_to==1:
        print("number", list[0])
        break
