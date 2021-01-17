# Import the os and csv module
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Set variables
NumOfMonths = 0
net_total = 0
greatestInc = 0
greatestDec = 0
total_change = 0

# Open 'budget_data.csv'

with open(csvpath) as csvfile:

    # CSV reader specifies delimeter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        
        # Count each month
        NumOfMonths = NumOfMonths + 1

        # Define current row's profit/loss
        current_row_total = row[1]

        # Add to or subtract from net total
        net_total = net_total + int(current_row_total)

        # Calculate the change in profit/loss over the entire period
        total_change = int(current_row_total) - total_change

        # Find greatest increase in profits and greatest decrease in losses over the entire period
        if int(current_row_total) > 0:
            if int(current_row_total) > greatestInc:
                greatestInc = int(current_row_total)
                greatestIncMon = row[0]
        elif int(current_row_total) < 0:
            if int(current_row_total) < greatestDec:
                greatestDec = int(current_row_total)
                greatestDecMon = row[0]

    # Calculate the average in profit/loss over the entire period
    avg_change = total_change / NumOfMonths

    print("")
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {NumOfMonths}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {greatestIncMon} (${greatestInc})')
    print(f'Greatest Decrease in Profits: {greatestDecMon} (${greatestDec})')

# Specify the file to write to
output_path = os.path.join("analysis", "pybank.txt")

file = open(output_path, "a")

file.write("Financial Analysis \n")
file.write("---------------------------- \n")
file.write(f'Total Months: {NumOfMonths} \n')
file.write(f'Total: ${net_total} \n')
file.write(f'Average Change: ${avg_change} \n')
file.write(f'Greatest Increase in Profits: {greatestIncMon} (${greatestInc}) \n')
file.write(f'Greatest Decrease in Profits: {greatestDecMon} (${greatestDec}) \n')
   