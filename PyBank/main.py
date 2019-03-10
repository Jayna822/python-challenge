# Modules
import os
import csv

# Set path for file
csvpath = 'budget_data.csv'

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    total_months = 0
    total_pnl = 0
    pnl_changes = []
    prev_pnl = None
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = None
    greatest_decrease_month = None

    for row in csvreader:
        current_month = row[0]
        current_pnl = int(row[1])

        total_months += 1
        total_pnl += current_pnl

        if prev_pnl:
            pnl_change = current_pnl - prev_pnl
            pnl_changes.append(pnl_change)

            if pnl_change > greatest_increase:
                greatest_increase = pnl_change
                greatest_increase_month = current_month
            if pnl_change < greatest_decrease:
                greatest_decrease = pnl_change
                greatest_decrease_month = current_month

        prev_pnl = current_pnl

avg_change = sum(pnl_changes) / len(pnl_changes)

print('Total Months: %d'%total_months)
print('Total PnL: %d'%total_pnl)
print('Average Change in PnL: %.2f'%avg_change)
print('Greatest Increase in Profits: %s (%d)'%(greatest_increase_month, greatest_increase))
print('Greatest Decrease in Profits: %s (%d)'%(greatest_decrease_month, greatest_decrease))
