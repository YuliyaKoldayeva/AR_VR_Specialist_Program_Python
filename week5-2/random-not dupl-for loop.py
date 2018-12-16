import random

list=[] # list with a range of unique sequential numbers in a desired interval
final_list=[] # list of unique random numbers

# ask for interval and the number of elements in the final list

minVal = int(input("Random numbers starting from >>>  "))
maxVal = int(input("Random numbers starting up to  >>>  "))
number_elements = int(input("How many elements do you want in your list >>>  "))

while maxVal- minVal+1 < number_elements:
    print("The number of elements in your list should be bigger or equal to the difference between the biggest and the smallest one.")
    number_elements = int(input("How many elements do you want in your list >>>  "))

# generate a list with a range of unique sequential numbers in a desired interval
for number in range(minVal,maxVal+1):
    list.append(number)

# generate a list of unique random numbers by randomly selecting them
# from our original ange of unique sequential numbers by cutting them form the original list
for number in range(number_elements):
    # up_to defines the max value in a range for choosing index randomly
    # it is done by adjusting the range of index still available in the list
    # maxVal-minVal - defines the number of elements of the first list
    # then the number of already cut element is subtracted
    up_to = ((maxVal-minVal)-number)
    index = random.randint(0,up_to)
    final_list.append(list.pop(index))
print("My list of random unique values is ", final_list)
