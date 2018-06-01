
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

    # total votes count, finding individual vote counts
    for row in csvreader:
        total_votes +=1
        if row[2] in candidates.keys():
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

# printing to the terminal
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

# creating new text file
new_file = open("Output/mypollresults1.txt", "w")

# writing the new file
new_file.write("Election Results \n")
new_file.write("------------------------------------- \n")
new_file.write("Total Votes: " + str(total_votes) + "\n")
new_file.write("------------------------------------- \n")
for key, value in candidates.items():
    new_file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
new_file.write("------------------------------------- \n")
new_file.write("Winner: " + winner + "\n")
new_file.write("------------------------------------- \n")#
