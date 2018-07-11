import csv
from collections import Counter

csvpath = "election_data.csv"
total_votes = 0
candidate_list = []
total_votes =[]
first_row = True
with open(csvpath, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = '\n')
	csv_header = next(csvfile)
	for row in csvreader:



# A complete list of candidates who received votes
#Separate the Voter ID,County and Candidate
		this_row = row[0].split(",")
		candidate_name = this_row[2]
		total_votes.append(candidate_name)
		if first_row is True:
			candidate_list.append(candidate_name)
			first_row = False
		
		if candidate_name not in candidate_list:
			candidate_list.append(candidate_name)

# The percentage of votes each candidate won
# print(type(Counter(candidate_vote)))
####### use dictionary
vote_counter = Counter(total_votes)
print(vote_counter)
print(list(vote_counter))
# The total number of votes cast
total_votes_counter = sum(vote_counter.values())

# The total number of votes each candidate won
# The winner of the election based on popular vote.
print("Election Results")
print ("----------------------")
print("Total Votes : " + str(total_votes_counter))
print ("----------------------")
