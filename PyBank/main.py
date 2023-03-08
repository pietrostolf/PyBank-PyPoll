import os
import csv
import numpy as np

data = []



budget_csv = os.path.join("PyBank","Resources","budget_data.csv")


with open(budget_csv, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    monthcount = 0
    net = 0
    next(csvfile)
    for row in csvreader:
        monthcount +=1
        net = int(row[1]) + net
        data.append(int(row[1]))
   
    changes = np.diff(data)
    average_change = np.mean(changes)
    mean = net / monthcount

    print(monthcount)
    print(net)
    print(f"Average Change:, {round(average_change,2)}")
    