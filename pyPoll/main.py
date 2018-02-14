#Expected Output Results
# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------

# You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). 
#Each dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of 
#the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.


#Don't forget to import csv
import csv
#import counter for use with percentage of votes
from collections import Counter


#link my csv file
f = open("raw_data/election_data_1.csv")
#set up my reader
reader = csv.DictReader(f)
#set up data to loop through multiple times
data = [row for row in reader]


#Now we can get started!
#print out the title
print("Election Results")
print("-----------------------")
#The total number of votes cast
#create an empty list to house totalVotes
totalVotes = []
#for loop to go through the csv 
for row in data:
	#then append each voter ID to the totalVotes list
	totalVotes.append(row["Voter ID"])
#nicely formatted total months
print("Total Votes: " + str(len(totalVotes)))
print("------------------------")


# A complete list of candidates who received votes
#create an empty list to house all candidates
allCandidates = []
#create an empty list to house filtered candidates
filteredCandidates = []
#for loop to go through the csv
for row in data:
	#then append every candidate to the candidates list
	allCandidates.append(row["Candidate"])
#Now, loop through allCandidates and append it to filtered candidates if its not already in it
for x in allCandidates:
	if x not in filteredCandidates:
		filteredCandidates.append(x)
#print the result
print("Candidates: " + str(filteredCandidates))
print("------------------------")


#percentage of votes each candidate won
#We already have the list allCandidates which has all the votes for each candidate. 
#we just need to find out how many each had, and then divide it by the total number of votes.
#set all candidates to a dictionary using the counter function
votesPerCan = dict(Counter(allCandidates))
#set canVotes equal to the values returned in the dictionary, converting it to a list
canVotes = list(votesPerCan.values())
#set canNames equal to the keys of the dictionary, converting it to a list
canNames = list(votesPerCan.keys())
k = 0
while k < len(canNames):
	print(canNames[k] + ":   " + str(int(int(canVotes[k]) / len(totalVotes) * 100)) + "%   " + "(" + str(int(canVotes[k])) + ")")
	k = k+1
print("------------------------")


# The winner of the election based on popular vote.
#find the index of the most votes from canVotes
winnerIndx = canVotes.index(max(canVotes))
#find the candidate name from the same index as the most votes
winner = canNames[winnerIndx]
#print your findings
print("Winner: " + str(winner))
print("------------------------")