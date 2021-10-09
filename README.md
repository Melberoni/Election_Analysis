# Election_Analysis

## Project Overview
A colorado Board of Elections employee has asked me to complete election results analysis by doing the following tasks:
1. Calculate the total number of votes
2. get a complete list of all candidates who recieved votes
3. calculate the total number of votes each candidate recieved
4. calculate the percentage of votes each candidate recived
5. determine the winner of the election based on popular vote
6. The voter turnout for each county
7. the percentage of votes from each county out of the total number of votes
8. the county with the highest turnout of voters

## Resources
- Data source:election_results.csv
- software Python 3.6.1, Visual studio code 1.61.0

## Summary
The analysis of the election show that:
- There were 369,711 Votes cast in the election

- The county results were:
  - Jefferson County had 10.5% of votes with a total count of 38,855 votes
  - Denver County had 82.8% of votes with a total count of 306,055 votes
  - Arapahoe County had 6.7% of votes with a total count of 24,801 votes
- Denver county had the largest number of votes at 306,055 votes

- The candidate results were:
  - Charles Casper Stockham recieved 23.0% of the vote with a total of 85,213 votes.
  - Diana DeGette recieved 73.8% of the vote with a total of 272,892 votes.
  - Raymon Anthony Doane recieved 3.1% of the vote with a total of 11,606 votes.
- The winner of the election was Diana DeGette, who recieved 73.8% of the vote and a total of 272,892 votes.

## Election-Audit Summary
The Election commission should be able to use this analysis python script to analyze any election in the future as it dynamically counts up the number of candidates and other variables. For example if you had an election for schoolboard members and you wanted to see which school district had the largest number of voter turnout we could easily replace the county variable with school district. Another example would be if you wanted to elect more than one candidate because you have multiple seats open on a board we could easily output a ranking of each candidate so it would be easy to see the top 2 (or more) votes.

