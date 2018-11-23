import random
my_list=[]
counter = 0
duplicate = 0

while True:
    if counter == 10:
        break
    else:
        duplicate = 0
        my_random_number = random.randint(1, 15)

        print("My random is ", my_random_number)

        for element in my_list:
            if my_random_number == element:
                duplicate += 1

        if duplicate < 1:
            my_list.append(my_random_number)
            counter += 1

print("Here is my list ", my_list)
