import os
import csv

#budget_data consistes of Date, Profit/Losses - dates are mmm/yy profit vs loss designated by positive or negative number
#Total number months - this is a count - you could actually count the profit/loss as it is a 1:1
#Net total - sum of P&L
#Ave change - Ave P&L
#Max profits
#Max decrease
# see example of Financial Analysis

#path for data - since already in resources I do not think I need to include path??
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Lists
Total_Months = []
Net_Total = []
Ave_Change = []

# read in csv file - with open does not require close -- looks like this is done at the end
row = []
with open(budget_csv, 'r') as csvfile:
    #split by commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #extract field names through first row
    header = next(csvreader)
    
    #init lists - starting value
    for row in csvreader:
        Total_Months.append(row[0])
        Net_Total.append(row[1])
        #net_change = int(row[1]) - prev_net ----must define


    print (row)


