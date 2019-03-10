import os
import csv

'''
Here's a solution using min() and max() as mentioned in the video.
See if you can walk through the code and figure out how it works!
'''

csvpath = 'budget_data.csv'

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    months = []
    total = 0
    changes = []
    last_total = None

    for row in csvreader:
        months.append(row[0])
        current_total = int(row[1])
        total += current_total
        if last_total:
            change = current_total - last_total
            changes.append(change)
        last_total = current_total

    average_change = sum(changes) / float(len(changes))
    greatest_increase = max(changes)
    greatest_increase_month = months[changes.index(greatest_increase) + 1]
    greatest_decrease = min(changes)
    greatest_decrease_month = months[changes.index(greatest_decrease) + 1]

print('Financial Analysis')
print('-----------------------')
print('Total Months: %d'%len(months))
print('Total: $%d'%total)
print('Average Change: $%.2f'%average_change)
print('Greatest Increase in Profits: %s ($%d)'%(greatest_increase_month, greatest_increase))
print('Greatest Decrease in Profits: %s ($%d)'%(greatest_decrease_month, greatest_decrease))
