# create file path across operating system
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'PyPoll_election_data.csv')
 
# Create variables for calculations
candidates = []
number_votes = 0
vote_counts = []

# Open current CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

        # Skip headers
    line = next(csvreader,None)

        # loop through the votes
    for line in csvreader:

            # Add to total number of votes
            number_votes = number_votes + 1

            # The candidate voted for
            candidate = line[2]

            # If the candidate has other votes then add to vote total
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1

            # Else create new spot in list for candidate
            else:
                candidates.append(candidate)
                vote_counts.append(1)

# Create variables for calculations
    percentages = []
    max_votes = vote_counts[0]
    max_index = 0

    # Percentage of vote for each candidate and the winner
    for count in range(len(candidates)):
        vote_percentage = vote_counts[count]/number_votes*100
        percentages.append(vote_percentage)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]

   # Print results of the vote and print the winner
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {number_votes}")
    for count in range(len(candidates)):
        print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------") 

     # sets path for output file
    output_file = os.path.join('Resources', 'pypoll_output.csv')
    
# opens the output destination in write mode and prints the summary
with open(output_file, 'w') as writefile:
    writefile.writelines('Election Results\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines(f'Total Votes: {number_votes}\n')
    for count in range(len(candidates)):
        writefile.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
    writefile.writelines('----------------------------\n')
    writefile.write(f"Winner: {winner}\n")
    writefile.write("---------------------------\n")

#opens the output file in r mode and prints to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())

    # Close file
    writefile.close()

