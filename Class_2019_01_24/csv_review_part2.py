import csv

csv.register_dialect('myDialect', lineterminator="\n")

lb_to_kg = 0.453592
inch_to_cm = 2.54

with open('biostats.csv', 'rt') as my_csv_file:
    reader = csv.reader(my_csv_file)

    with open('biostats_SI.csv', 'w') as my_csv_file:
        writer = csv.writer(my_csv_file, dialect='myDialect')

        for row in reader:
            new_line = []
            new_line.append(row[0])
            new_line.append(row[1])
            new_line.append(row[2])

            try:
                adj_height = int(row[3]) * inch_to_cm
                adj_weight = int(row[4]) * lb_to_kg
                bmi = adj_weight / (adj_height*adj_height) * 10000
                new_line.append(int(adj_height))
                new_line.append(int(adj_weight))
                new_line.append(int(bmi))

            except:
                new_line.append("Height(cm)")
                new_line.append("Weight(kg)")
                new_line.append("BMI")

            writer.writerow(new_line)
