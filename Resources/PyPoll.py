import os
import csv
#import statistics for mode function
import statistics

#path for data
election_csv = os.path.join('Resources', 'election_data.csv')

# read in csv file
with open(election_csv, 'r') as csvfile:
    #split by commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #extract field names through first row
    header = next(csvreader)

    #set start values
    Candidates = []
    Total_Votes = 0    
    
    #loop for Total_Votes and create candidate list
    for row in csvreader:
        Total_Votes += 1
        Candidates.append(row[2])


    #candidates with votes list - hum all candidates have votes   
    candidate_list = list(set(Candidates))

    #define and summarize results
    def results(candidate_name):
        #store votes per candidate
        candidate_votes = int(0)

        #Loop through candidates
        for row in Candidates:
            if candidate_name == row:
                candidate_votes += 1

        #calculation for percentage of votes per candidate
        percentage = round((candidate_votes / Total_Votes)*100, 2)
        return "{}: {}% ({})".format(candidate_name, percentage, candidate_votes)

# winner formula
winner = statistics.mode(Candidates)

#print(f"Average Change: {Average_Change}")
print(f"Election Results")
print(f"-----------------")
print(f"Total Votes: {Total_Votes}")
print(f"------------------------------")
print(results('Khan'))
print(results('Correy'))
print(results('Li'))
print(results("O'Tooley"))
print(f"------------------")
print('Winner: {}'.format(winner))

#set variable for results file
results_file = os.path.join("Analysis", "PyPoll_Analysis.txt")

#open output file and create header row then write to textfile
with open(results_file, 'w') as textfile:
    textfile.write(f"Election Results\n")
    textfile.write(f"-------------------\n")
    textfile.write(f"Total Votes: {Total_Votes}\n")
    textfile.write(("{}\n".format(results('Khan'))))
    textfile.write(("{}\n".format(results('Correy'))))
    textfile.write(("{}\n".format(results('Li'))))
    textfile.write(("{}\n".format(results("O'Tooley"))))
    textfile.write(f"---------------------------------\n")
    textfile.write(f"Winner: {winner})")
