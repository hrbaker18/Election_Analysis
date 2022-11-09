#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable for the file to load and the path.
file_to_save = os.path.join("Resources", "election_results.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
    
    # Print the candidates name from each row
        candidate_name = row[2]
        # print(candidate_name)

        if candidate_name not in candidate_options:

            # Add the candidates name to the candidate list
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    
    
# Print the candidate votes dictionary
    # print(candidate_votes)
    

#  To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.

    
    # Determine if the votes is greater than the winning count.
#  To do: print out the winning candidate, vote count and percentage to
#   terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage

        # Print the winning candidate to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_candidate_summary)
