import csv
from collections import Counter

csvpath = "election_data.csv"
title = "Election Results"
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
vote_counter = Counter(candidate_list)
total_votes = sum(vote_counter.values())
print(title)
print ("-"* 25)
print("Total Votes : " + str(total_votes))
print ("-"* 25)
for key, value in vote_counter.items():
	print("{}: {}% ({})".format(key, round((value/total_votes*100),3), value))
	if votes < value:
		winner = key
		votes = value
print ("-"* 25)
print("Winner : " + winner)
print ("-"* 25)

output_file = "output.txt"
with open(output_file, 'w', newline = "") as datafile:
	writer = csv.writer(datafile)
	writer.writerow([title])
	writer.writerow(["-"* 25])
	writer.writerow(["Total Votes : " + str(total_votes)])
	writer.writerow(["-"* 25])
	for key, value in vote_counter.items():
		writer.writerow(["{}: {}% ({})".format(key, round((value/total_votes*100),3), value)])
	writer.writerow(["-"* 25])
	writer.writerow(["Winner : " + winner])
	writer.writerow(["-"* 25])


