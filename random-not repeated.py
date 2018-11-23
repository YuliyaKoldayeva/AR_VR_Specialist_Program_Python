import random
list=[] # list with a range of unique sequential numbers in a desired interval
final_list=[] # list of unique random numbers

# ask for interval and the number of elements in the final list
number_elements = int(input("How many elements do you want in your list >>>  "))
minVal = int(input("MIN value of your random numbers >>>  "))
maxVal = int(input("MAX value of your random numbers >>>  "))

# generate a list with a range of unique sequential numbers in a desired interval
for number in range(minVal,maxVal+1):
    list.append(number)

# generate a list of unique random numbers by randomly selecting them
# from our original ange of unique sequential numbers
for number in range(number_elements):
    up_to = ((maxVal-minVal)-number)
    index = random.randint(0,up_to)
    final_list.append(list.pop(index))
print("My list of random unique values is ", final_list)



"""
import random
list=[]
final_list=[]
number_elements = int(input("How many elements do you want in your list >>>  "))
minVal = int(input("MIN value of your random numbers >>>  "))
maxVal = int(input("MAX value of your random numbers >>>  "))
for number in range(minVal,maxVal+1):
    list.append(number)
print("My initial list ", list)

for number in range(number_elements):
    print("xxxxxxx")
    up_to = ((maxVal-minVal)-number)
    print("up_to ", up_to)
    index = random.randint(0,up_to)
    print("index ", index)
    final_list.append(list.pop(index))
    print("My initial list ", list)
    print("My list of random unique values is ", final_list)
"""
