# Modules
import os
import csv

# Set path for file
csvpath = 'election_data.csv'

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # In the video, I created the below variable, but we actually don't need it
    # We could just sum up the values in the dictionary after the for-loop
    # In any case, it's up to you. I wouldn't say this makes the code less efficient,
    #   maintainable, or readable. So your call.
    total_votes = 0
    candidates = {}

    for row in csvreader:
        candidate = row[2]

        total_votes += 1

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

number_of_dashes = 25
print('Election Results')
print('-' * number_of_dashes)
print('Total Votes: %d'%total_votes)
print('-' * number_of_dashes)

highest_number_of_votes = 0
winner = None
for candidate, votes in candidates.items():
    percentage = votes / total_votes * 100
    print('%s: %.2f%% (%d)'%(candidate, percentage, votes))
    if votes > highest_number_of_votes:
        winner = candidate
        highest_number_of_votes = votes
print('-' * number_of_dashes)
print('Winner: %s'%winner)
