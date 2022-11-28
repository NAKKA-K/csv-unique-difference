import csv
import pprint

with open("./sample.csv", "r") as csv_file:
    # f = csv.reader(csv_file, delimiter=",", doublequote=True, skipinitialspace=True)
    print(csv_file.read())
