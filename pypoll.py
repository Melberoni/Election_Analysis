#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote



import csv
import os


# assign a variable for the file to load and the path
#file_to_load="resources/election_results.csv"
file_to_load=os.path.join("resources","election_results.csv")
#assign a variable to save the file to a path
file_to_save=os.path.join("analysis", "election_analysis.txt")
candidate_options=[]
candidate_votes={}
#initialize the vote counter
total_votes=0
#track winning candidate
winning_candidate=''
winning_count=0
winning_percentage=0
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

with open(file_to_save, "w") as txt_File:
    header_output=(
        f"Election Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n" )
    print(header_output,end="")
        #save the final fvote ocunt ot the output txt file
    txt_File.write(header_output)


    for candidate_name in candidate_votes:
        votes=candidate_votes[candidate_name]
        vote_percentage=float(votes)/float(total_votes)
        
        #print each candoidate and their vote and percentage to terminal
        candidate_results=(f"{candidate_name}: {vote_percentage:.1%} ({votes:,})\n")
        print(candidate_results)
        #save results to output txt file
        txt_File.write(candidate_results)

        #determine if the votes are grater than the winning ocunt if so then reset the winning information
        if (votes > winning_count) and (vote_percentage>winning_percentage) :
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
    #summerize the winning candidate and print it out to terminal
    winning_candidate_summary=(
        f"------------------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning vote Count: {winning_count:,}\n"
        f"Winning Percentage:{winning_percentage:.1%}%\n"
        f"-------------------------------------\n")
    txt_File.write(winning_candidate_summary)
