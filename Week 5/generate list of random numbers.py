import random
my_list=[]
for number in range(10):
    my_list.append(random.randint(1,100))
print("Here is my list ", my_list)

# find the MAX
max_value = my_list[0]
for item in my_list:

    if item > max_value:
        max_value = item
print("MAX value is: ", max_value)

# find the MIN
min_value = my_list[0]
for item in my_list:

    if item < min_value:
        min_value = item
print("MIN value is: ", min_value)

# My list length
list_length = 0
for item in my_list:
    list_length+=1
print("My list length is : ", list_length)

# Sum of all elements
sum_elements = 0
for item in my_list:
    sum_elements = sum_elements+item
print("Sum of all elements is : ", sum_elements)


# Finding average
"""
try:
    sum_elements / list_length
except ZeroDivisionError:
    print("Zero Div")
else:
    print("The average value of elements of this list is : ", sum_elements/list_length)
    """
print("The average value of elements of this list is : ", sum_elements/list_length)


