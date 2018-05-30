# import operating systems and csv file
import os
import csv

# set the file path
csvpath = os.path.join('Resources','election_data_1.csv')

# tracking variables
total_votes = 0
candidates = {}
candidates_percent = {}
winner = ""
winner_count = 0

# read the file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader,None)

    # total vote count; finding individual vote counts
    for row in csvreader:
        total_votes +=1
        if row[2] in candidates.key():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

# percentages for each candidate
for key, value in candidates.items():
    candidates_percent[key] = round((value/total_votes) * 100,2)

# to find the winner
for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

# tests
print(total_votes)
