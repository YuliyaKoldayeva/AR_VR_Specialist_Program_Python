# Summ ages
age1 = 20
age2 = 20
print("The sum of the ages is {}".format(age1+age2))

# Champlain

name = "champlain"
print("I am taking this course at {}".format(name.title()))

# Total price
price1 = "1.40"
price2 = "2.30"
# transform each price string to a numeric value
price1_float = float(price1)
price2_float = float(price2)
# reducing the number of digits after decimal
total_price= "{0:.2f}".format(price1_float+price2_float)
print("The total sale price is {}".format(total_price))

# importing decimal

import decimal
price1 = "1.40"
price2 = "2.30"
price1_decimal = decimal.Decimal(price1)
print(price1_decimal)

# percentage
total = 34.00
increase_rate = 1.1556
print("The total amount increased by the percentage rate is: {}".format(total*increase_rate))

# variables
var1 = "hello"
var2 = "you"
print("The length of both of the variables var1 and var2 is {} characters".format(len(var1+var2)))

# square numbers
print("Square numbers from 1 to 100:")
for number in range(1,11):
    print(number**2)

# all possible combinations of 0 and 1
print("All possible combinations of 0 and 1")
for number1 in range(2):
    for number2 in range(2):
        for number3 in range(2):
            print("{}{}{}".format(number1,number2,number3))