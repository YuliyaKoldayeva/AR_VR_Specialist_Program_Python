import csv

order_counter=0
units_sold = 0
item_type = set()

with open('7_-_100_Sales_Records.csv', 'rt') as my_csv_file:
    reader = csv.reader(my_csv_file)
    next(reader) # The call to next reads the first row and discards it.

    for row in reader: # iterate through the actual data (without the header)
        units_sold +=int(row[8])
        item_type.add(row[2])
        if row[0]=='Europe':
            order_counter+=1
    print("There are {} order records from Europe".format(order_counter))
    print("The total of units sold is {}".format(units_sold))
    print("The list of item types without duplicates is the following: \n", item_type)