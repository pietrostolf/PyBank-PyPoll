#import dependencies
import os
import csv
import numpy as np

#create lists for dates and profit_losses data
data = []
date = []


#define csv path
budget_csv = os.path.join("Resources","budget_data.csv")

#open csv
with open(budget_csv, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    monthcount = 0
    net = 0
    next(csvfile)

#iterate through csv rows and find results
    for row in csvreader:
        monthcount +=1
        net = int(row[1]) + net
        data.append(int(row[1]))
        date.append(row[0])

#find changes in dataset        
    changes = np.diff(data)
    average_change = np.mean(changes)
    mean = net / monthcount
    min_pos = np.argmin(changes)
    max_pos = np.argmax(changes)

#display results on the console
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {monthcount}")
print(f"Total: {net}")
print(f"Average Change:, ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {date[max_pos+1]} (${max(changes)})")
print(f"Greatest Decrease in Profits: {date[min_pos+1]} (${min(changes)})")

#generate txt file with results
with open('analysis/output.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("-----------------------------------\n")
    f.write(f"Total Months: {monthcount}\n")
    f.write(f"Total: {net}\n")
    f.write(f"Average Change: ${round(average_change,2)}\n")
    f.write(f"Greatest Increase in Profits: {date[max_pos+1]} (${max(changes)})\n")
    f.write(f"Greatest Decrease in Profits: {date[min_pos+1]} (${min(changes)})\n")
