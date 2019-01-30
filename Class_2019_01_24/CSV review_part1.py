import csv

ages_sum = 0
female_counter = 0
respondents_counter = 0

with open('biostats.csv', 'rt') as my_csv_file:
    reader = csv.reader(my_csv_file)
    next(reader) # The call to next reads the first row and discards it.

    for row in reader: # iterate through the actual data (without the header)

        respondents_counter += 1
        ages_sum += int(row[2])

        if row[1] == "F":
            female_counter += 1

average_age = ages_sum/respondents_counter
female_percentage = (female_counter/respondents_counter)*100
male_percentage = 100 - female_percentage

print("The percentage of female respondents is {:0,.2f} %.".format(female_percentage))
print("The percentage of male respondents is {:0,.2f} %.".format(male_percentage))
print("The average age of all respondents is {:0,.2f} years.".format(average_age))
