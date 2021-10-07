#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote


import datetime
import csv
import random
import os
#import numpy

# assign a variable for the file to load and the path
#file_to_load="resources/election_results.csv"
file_to_load=os.path.join("resources","election_results.csv")
#assign a variable to save the file to a path
file_to_save=os.path.join("analysis", "election_analysis.txt")


#open the election results and read the file
with open(file_to_load) as election_data:

    #read the file object with reader function
    file_reader=csv.reader(election_data)
    headers=next(file_reader)
    print(headers)
    #print each row in the csv file
    #for row in file_reader:
        


#open file to save as txt
with open(file_to_save,"w") as txt_file:
    
    #write data to the file
    txt_file.write("Counties in the election\n")
    txt_file.write("--------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
