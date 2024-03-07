import os
import csv

Poll_path = os.path.join('Resources', 'election_data.csv')
output_file_path = os.path.join('Resources', 'election_results.txt')

# Count number of votes
total_votes = 0
candidates_votes = {}

with open(Poll_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    rows = list(csvreader)
    header = rows[0]

    # Assuming the column index for 'Candidate' is 2 and 'Votes' is 0, adjust if needed
    vote_column_index = 0
    candidate_column_index = 2

    # Iterate through rows and extract vote information
    for row in rows[1:]:
        vote = row[vote_column_index]
        total_votes += 1

        candidate = row[candidate_column_index]

        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1

print("Election Results")
print("-------------------")
print(f'Total Votes: {total_votes}')
print("-------------------")
print("List of Candidates:")
for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    print(f'{candidate}: {votes} votes ({percentage:.2f}%)')

print("-------------------")

# Find the winner
winner = max(candidates_votes, key=candidates_votes.get)
print(f'Winner: {winner}')

with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------\n")
    output_file.write(f'Total Votes: {total_votes}\n')
    output_file.write("-------------------\n")
    output_file.write("List of Candidates:\n")
    for candidate, votes in candidates_votes.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f'{candidate}: {votes} votes ({percentage:.2f}%)\n')
    output_file.write("-------------------\n")
    output_file.write(f'Winner: {winner}\n')