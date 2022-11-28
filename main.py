import csv
import pprint

with open("./sample.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
