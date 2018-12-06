"""
Ask the user to type the province
"""

provinces = {'QC': "Quebec", 'ON':'Ontario', 'BC': "British Colambis"}

code = input("Please type the province code ")

code_formatted = code.upper()

if code_formatted in provinces:
    print("My test name of the province is", provinces[code_formatted])
else:
    print("This code is not in the provinces list")

"First solution"

if code_formatted in provinces.keys():
    print("The name of the province is", provinces[code_formatted])
else:
    print("This code is not in the provinces list")

"Second solution"

try:
    code_formatted in provinces.keys()
    print("The name of the province is", provinces[code_formatted])
except KeyError:
    print("This code is not in the provinces list")
