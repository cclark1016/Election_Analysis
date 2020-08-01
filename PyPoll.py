# Add our dependencies
import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join('Resources','election_results.csv')
#Assign a variable to save the file to a path
file_to_save = os.path.join('analysis','election_analysis.txt')

#1. Initialize total vote counter
total_votes = 0
#candidate options
candidate_options = []
#candidate votes
candidate_votes = {}
winning_candidate= ""
winning_count = 0
winning_percentage = 0
#open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)


    #print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        #get candidate name
        candidate_name = row[2]
        #add candidate name to candidate list if they dont match existing
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #begin tracking that candidates votes count
            candidate_votes[candidate_name] = 0
        #add a vote to candidates count
        candidate_votes[candidate_name] += 1
    
    #Determine the percentage of votes for each candidate by looping through the counts
    #1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2. retrieve vot count of a candidate
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # print
        print(f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")

         #Winning Candidate and Winning Count Tracker
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    print(f"-------------------------------\n")
    print(f"{winning_candidate} has won the election with {winning_count:,} votes and {winning_percentage:.2f}% of the electorate")


      







