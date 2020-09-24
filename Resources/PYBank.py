import os
import csv

#path for data
budget_csv = os.path.join('Resources', 'budget_data.csv')

# read in csv file
with open(budget_csv, 'r') as csvfile:
    #split by commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #extract field names through first row
    header = next(csvreader)

    #Lists and starting variables
    Month = []
    Average_Change = []
    PL = []
    PL_Change = []
    Total_PL_Change = []

    #populate my month and PL lists by reading the csv
    for row in csvreader:
        #init my Total_Months
        Month.append(row[0])
        PL.append(int(row[1]))
    #month count
    Total_Months = (len(Month))       
    
    #PL
    PL_int = map(int,PL)
    Total_PL = (sum(PL))
       
    #Changes in PL
    i = 0
    for i in range(len(PL) -1):
        PL_Change = int(PL[i+1]) - int(PL[i])
        Total_PL_Change.append(PL_Change)
    Total_Change = sum(Total_PL_Change)
    Average_Change = round(Total_Change / len(Total_PL_Change), 2)
     
#calculate the min and max of the change
Max_Increase = max(Total_PL_Change)
Max_Decrease = min(Total_PL_Change)

#Final print the report
print(f"Financial Analysis")
print(f"-------------------")
print(f"Total Months: {Total_Months}")
print(f"Average Change: {Average_Change}")
print(f"Greatest increase in Profits: {Max_Increase}")
print(f"Greatest decrease in Profits: {Max_Decrease}")

#set variable for results file
results_file = os.path.join("Analysis", "PyBank_Analysis.txt")

#open output file and create header row then write to textfile
with open(results_file, 'w') as textfile:
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"-------------------\n")
    textfile.write(f"Total Months:{Total_Months}\n")
    textfile.write(f"Average Change: {Average_Change}\n")
    textfile.write(f"Greatest increase in Profits: {Max_Increase}\n")
    textfile.write(f"Greatest decrease in Profits: {Max_Decrease}\n")
  