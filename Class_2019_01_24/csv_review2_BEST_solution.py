import csv

csv.register_dialect('myDialect', lineterminator="\n")

lb_to_kg = 0.453592
inch_to_cm = 2.54

with open('biostats.csv', 'rt') as my_csv_file:
    reader = csv.reader(my_csv_file)

    with open('biostats_METRIC.csv', 'w') as my_csv_file:
        writer = csv.writer(my_csv_file, dialect='myDialect')

        for row in reader:

            try:
                row[3] = int(int(row[3]) * inch_to_cm)
                row[4] = int(int(row[4]) * lb_to_kg)

            except:
                if row[0] == "Name":
                    row[3] = "Height(cm)"
                    row[4] = "Weight(kg)"
                else:
                    print("Data is not numeric")

            new_line = row

            writer.writerow(new_line)
