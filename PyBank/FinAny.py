# -*- coding: utf-8 -*-
"""byBank Home work
this script is for analyzing the financial records of a company. The input is the budget_data.csv. This dataset is composed of two columns, Date and Profit/Losses. 
The script analyzes the records to calculate each of the following:
-The total number of months included in the dataset.
-The net total amount of Profit/Losses over the entire period.
-The average of the changes in Profit/Losses over the entire period.
-The greatest increase in profits (date and amount) over the entire period.
-The greatest decrease in losses (date and amount) over the entire period.
"""

# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path('budget_data.csv')

# Initialize list of records
records = []

# Open the csv file as an object
with open(csvpath, 'r') as csvfile:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # Set the 'num_months', 'net_profit_loss', and 'ave_chg_profit_loss, greatest_profit, greatest_loss' variables for better
        # readability, convert strings to ints for numerical calculations
    num_months = 0
    profit_loss = int(next(csvreader)[1])
    net_profit_loss = profit_loss
    total_chg_profit_loss = 0
    greatest_profit = 0
    greatest_loss = 0
    # Read each row of data after the header
    for row in csvreader:
        
        # Set the 'num_months', 'net_profit_loss', and 'ave_chg_profit_loss, greatest_profit, greatest_loss' variables for better
        # readability, convert strings to ints for numerical calculations
        num_months = num_months + 1
        next_profit_loss = int(row[1])
        net_profit_loss = net_profit_loss + next_profit_loss
        chg_profit_loss = next_profit_loss-profit_loss
        total_chg_profit_loss = chg_profit_loss + total_chg_profit_loss 
         
        if (chg_profit_loss >= 0) and (chg_profit_loss>greatest_profit):
            greatest_profit = chg_profit_loss
            greatest_profit_date = str(row[0])
        elif (chg_profit_loss < 0)and (chg_profit_loss<greatest_loss):
            greatest_loss = chg_profit_loss
            greatest_loss_date = str(row[0])
        profit_loss=next_profit_loss
        # Calculate the average and round to the nearest 2 decimal places
    ave_chg_profit_loss = round(total_chg_profit_loss / num_months, 2)

print("Financial Analysis")
print("---------------------------------") 
print(f"Total Months: {num_months}")
print(f"Total : ${net_profit_loss}")
print(f"Average Change: $({ave_chg_profit_loss})")
print(f"Greatest Increase in Profit: {greatest_profit_date} $({greatest_profit})")
print(f"Greatest Decrease in Profit: {greatest_loss_date} $({greatest_loss})")
# Set the path for the output.txt
output = open(r"output.txt", "w+")
output.write("Financial Analysis\n")
output.write("---------------------------------\n") 
output.write(f"Total Months: {num_months}\n")
output.write(f"Total : ${net_profit_loss}\n")
output.write(f"Average Change: $({ave_chg_profit_loss})\n")
output.write(f"Greatest Increase in Profit: {greatest_profit_date} $({greatest_profit})\n")
output.write(f"Greatest Decrease in Profit: {greatest_loss_date} $({greatest_loss})\n")
output.close()
# Open the output path as a file and pass into the 'csv.writer()' function
# Set the delimiter/separater as a ','

