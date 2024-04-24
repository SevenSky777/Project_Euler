import time
import csv

strt = time.perf_counter()

with open('./gridnumbers.csv') as gridfile:
    grid_reader = csv.reader(gridfile, delimiter=' ')
    for line in grid_reader:
        print(line)

endt = time.perf_counter()
print(endt-strt)
