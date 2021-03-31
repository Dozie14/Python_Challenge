import os
import csv

# Path to collect data from the Resources folder
budgetdata_csv = os.path.join('Resources', 'budget_data.csv')




# Read in the CSV file
with open(budgetdata_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the column names in the data
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        print(row)
