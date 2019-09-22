# create file path across operating systems
import os

# Module for reading csv files
import csv
csvpath = os.path.join('Resources', 'PyBank_Budget_data.csv')

# lists to be analyzed/reported 
months = []
profits = []
date = []

# read csv and parse data into lists
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    
    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))

# find total months
total_months = len(months)

# create greatest increase and decrease in profits as a variable
greatest_inc = profits[0]
greatest_dec = profits[0]
total_profits = 0

# loop through profits indices and compare to find greatest increase and decrease
for r in range(len(profits)):
    if profits[r] >= greatest_inc:
        greatest_inc = profits[r]
        great_inc_month = months[r]
    elif profits[r] <= greatest_dec:
        greatest_dec = profits[r]
        great_dec_month = months[r]
    total_profits += profits[r]

# calculate average_change
average_change = round(total_profits/total_months, 2)

#sets path for output file
output_pybank = os.path.join('Resources', 'pybank_output.csv')

# opens the output destination in write mode and prints the summary
with open(output_pybank, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Profits: $' + str(total_profits) + '\n')
    writefile.writelines('Average Profits Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Profits: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Profits: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

# opens the output file in r mode and prints to terminal
with open(output_pybank, 'r') as readfile:
    print(readfile.read())

# Close file
    writefile.close()
