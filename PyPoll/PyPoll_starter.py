# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  

# Track the total number of votes cast
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = "" # Tracker for the winning candidate 
max_votes = 0 # Tracker for the maximum votes

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        voter_id = row[0] 
        candidate = row[2]

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1


        # Get the candidate's name from the row
        # If the candidate is not already in the candidate list, add them
        # Add a vote to the candidate's count
        if candidate not in candidate_votes: 
            candidate_votes[candidate] = 0 
        candidate_votes[candidate] += 1



# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}\n")


    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")


    # Loop through the candidates to determine vote percentages and identify the winner
        # Get the vote count and calculate the percentage
        # Update the winning candidate if this one has more votes
        # Print and save each candidate's vote count and percentage
    
    winner = "" 
    max_votes = 0 
    for candidate, votes in candidate_votes.items(): 
        percentage = (votes / total_votes) * 100 
        print(f"{candidate}: {percentage:.3f}% ({votes})") 
        txt_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n") 
        
        if votes > max_votes: 
            max_votes = votes 
            winner = candidate



    # Generate and print the winning candidate summary
    print(f"Winner: {winner}\n")


    # Save the winning candidate summary to the text file
    txt_file.write(f"Winner: {winner}\n")
