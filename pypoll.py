#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote


import datetime
import csv
import random
import os
from typing import Counter
#import numpy

# assign a variable for the file to load and the path
#file_to_load="resources/election_results.csv"
file_to_load=os.path.join("resources","election_results.csv")
#assign a variable to save the file to a path
file_to_save=os.path.join("analysis", "election_analysis.txt")
candidate_options=[]
candidate_votes={}
#initialize the vote counter
total_votes=0
#open the election results and read the file
with open(file_to_load) as election_data:

    #read the file object with reader function
    file_reader=csv.reader(election_data)
    #read the header row
    headers=next(file_reader)
    
    #print each row in the csv file
    for row in file_reader:
       # add to the total vote Count
        candidate_name=row[2]
#check and see if name is in list, if not add it
        if candidate_name not in candidate_options:
           
            candidate_options.append(candidate_name)
#start counting votes with a zero
            candidate_votes[candidate_name]=0

        candidate_votes[candidate_name]+=1
        total_votes+=1

winning_candidate=''
winning_count=0
winning_percentage=0

for candidate_name in candidate_votes:
    votes=candidate_votes[candidate_name]
    vote_percentage=float(votes)/float(total_votes)
    print(f"{candidate_name}: {vote_percentage:.1%} ({votes:,})\n")

    #determine if the votes are grater than the winning ocunt if so then reset the winning information
    if (votes > winning_count) and (vote_percentage>winning_percentage) :
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name
winning_candidate_summary=(
    f"------------------------------------\n"
    f"Winner:{winning_candidate}\n"
    f"Winning vote Count: {winning_count:,}\n"
    f"Winning Percentage:{winning_percentage:.1%}%\n"
    f"-------------------------------------\n")
print(winning_candidate_summary)

"""
#open file to save as txt
with open(file_to_save,"w") as txt_file:
    
    #write data to the file
    txt_file.write("Counties in the election\n")
    txt_file.write("--------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
"""