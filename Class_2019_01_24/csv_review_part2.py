import csv

ages_sum = 0
female_counter = 0
respondents_counter = 0

with open('biostats.csv', 'rt') as my_csv_file:

    writer = csv.writer(my_csv_file, delimiter=',')

    writer.writerows(csvData)
