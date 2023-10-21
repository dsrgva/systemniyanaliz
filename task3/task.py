import csv
from math import log2

def task(csv_string):
    csv_string = csv_string.split('\n')
    reader = csv.reader(csv_string)
    n = len(csv_string)
    entropy_value = 0
    for row in reader:
        row_entropy = 0 
        for value in map(int, row):
            if value != 0:
                element_entropy = value / (n - 1) * log2(value / (n - 1))
                row_entropy += element_entropy
        entropy_value -= row_entropy
    return round(entropy_value, 1)

print(task("1,0,4,0,0\n2,1,2,0,0\n2,1,0,1,1\n0,1,0,1,1\n0,1,0,2,1\n0,1,0,2,1"))
