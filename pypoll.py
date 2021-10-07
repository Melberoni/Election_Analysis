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


#open the election results and read the file
with open(file_to_load) as election_data:

    print(election_data)