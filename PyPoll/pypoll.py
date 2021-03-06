import csv
import os

election_data = os.path.join("Resources", "election_data.csv")
output = os.path.join("output.txt")

votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}


with open(election_data) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        votes = votes + 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 1

        else:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    # Determine the Winner:
    if (votes > winner_votes):
        greatest_votes[1] = candidate_votes
        greatest_votes[0] = row[2]

    election_analysis = "Election Results\n-------------------------\nTotal Votes: {}\n-------------------------".format(str(votes))
    for candidate in candidate_votes:
        election_analysis += str("\n"+candidate + " " + str(round(
            ((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    winner = sorted(candidate_votes.items(),)  
    election_analysis += str("\n-------------------------\nWinner: " + str(winner[1]))
    print(election_analysis)

# Output Files
    with open(output, "w") as txt_file:

        txt_file.write(election_analysis)