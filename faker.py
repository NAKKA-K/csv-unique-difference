import csv
import random

with open('./data/sample.csv', 'w') as f:
    writer = csv.writer(f)
    for i in range(400000):
        writer.writerow([random.randint(100000000, 500000000), 1%5*5])
    random.seed(0)
    for i in range(100000):
        writer.writerow([random.randint(100000000, 500000000), 1%5*5])

with open('./data/dlved.csv', 'w') as f:
    writer = csv.writer(f)
    random.seed(0)
    for i in range(100000):
        writer.writerow([random.randint(100000000, 500000000)])
