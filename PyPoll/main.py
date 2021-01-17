# Import the os and csv module
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Set variables
total_votes = 0
k = 0
c = 0
l = 0
o = 0
i = 0
winning_num = 0
candidates = []
votes = []

# Open 'election_data.csv'

with open(csvpath) as csvfile:

    # CSV reader specifies delimeter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        # Count each vote 
        total_votes = total_votes + 1

        # Create list of candidates who received votes
        if row[2] not in candidates:
            
            candidates.append(row[2])
        
        # Count votes for each candidate
        if row[2] == "Khan":

            k = k + 1

        elif row[2] == "Correy":

            c = c + 1

        elif row[2] == "Li":

            l = l + 1

        elif row[2] == "O'Tooley":

            o = o + 1
    
    votes.append(k)
    votes.append(c)
    votes.append(l)
    votes.append(o)

    for x in votes:
        
        if votes[i] > winning_num:

            winning_num = votes[i]
        
        i = i + 1

    if winning_num == k:

        winner = "Khan"

    elif winning_num == c:

        winner = "Correy"

    elif winning_num == l:

        winner = "Li"
    
    elif winning_num == o:

        winner = "O'Tooley"


    # Calculate the percentage of votes each candidate had won
    k_percent = '{:.3%}'.format(k / total_votes)
    c_percent = '{:.3%}'.format(c / total_votes)
    l_percent = '{:.3%}'.format(l / total_votes)
    o_percent = '{:.3%}'.format(o / total_votes)

    print("")
    print("Election Results")
    print("----------------------------")
    print("")
    print(f'Total Votes: {total_votes}')
    print("")
    print("----------------------------")

    for z in candidates:

        if z == "Khan":

            print(f'Khan: {k_percent} ({k})')

        elif z == "Correy":

            print(f'Correy: {c_percent} ({c})')
        
        elif z == "Li":

            print(f'Li: {l_percent} ({l})')

        elif z == "O'Tooley":

            print(f"O'Tooley: {o_percent} ({o})")
    
    print("----------------------------")
    print("")
    print(f'Winner: {winner}')
    print("")
    print("----------------------------")

# Specify the file to write to
output_path = os.path.join("analysis", "pypoll.txt")

file = open(output_path, "a")

file.write("\n")
file.write("Election Results\n")
file.write("----------------------------\n")
file.write("\n")
file.write(f'Total Votes: {total_votes}\n')
file.write("\n")
file.write("----------------------------\n")

for z in candidates:

    if z == "Khan":

        file.write(f'Khan: {k_percent} ({k})\n')

    elif z == "Correy":

        file.write(f'Correy: {c_percent} ({c})\n')
        
    elif z == "Li":

        file.write(f'Li: {l_percent} ({l})\n')

    elif z == "O'Tooley":

        file.write(f"O'Tooley: {o_percent} ({o})\n")
    
file.write("----------------------------\n")
file.write("\n")
file.write(f'Winner: {winner}\n')
file.write("\n")
file.write("----------------------------\n")
