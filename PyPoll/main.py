import csv
from collections import Counter

csvpath = "election_data.csv"
total_votes = 0
candidate_list = []
first_row = True
votes = 0
with open(csvpath, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = '\n')
	csv_header = next(csvfile)
	for row in csvreader:
#Separate the Voter ID,County and Candidate
		this_row = row[0].split(",")
		candidate_list.append(this_row[2])
#Create a counter variable 
vote_counter = Counter(candidate_list)
#Total no. of votes
total_votes = sum(vote_counter.values())
print("Election Results")
print ("-"* 25)
print("Total Votes : " + str(total_votes))
print ("-"* 25)
#Iterate through the counter variable and find the number of votes for each candidate and te winner
for key, value in vote_counter.items():
	print("{}: {}% ({})".format(key, round((value/total_votes*100),3), value))
	if votes < value:
		winner = key
		votes = value
print ("-"* 25)
print("Winner : " + winner)
print ("-"* 25)

#Writing to a txt file
output_file = "output.txt"
with open(output_file, 'w') as textfile:
	textfile.write("Election Results \n")
	textfile.write("-"* 25 +'\n')
	textfile.write("Total Votes : " + str(total_votes) +'\n')
	textfile.write("-"* 25 +'\n')
	for key, value in vote_counter.items():
		textfile.write("{}: {}% ({})".format(key, round((value/total_votes*100),3), value) +'\n')
	textfile.write("-"* 25 +'\n')
	textfile.write("Winner : " + winner +'\n')
	textfile.write("-"* 25 +'\n')
	


