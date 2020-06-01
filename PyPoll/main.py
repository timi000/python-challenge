import os
#Reaching the CSV File
csvpath= os.path.join("..","Resources","election_data.csv")
#Creating Lists for Voter IDs, County, Candidatesvotes,Candidates List
VoterID=[]
County=[]
Candidatevotes=[]
Candidateslist =[]
#Creating Counters for the Candidate's votes
KhanVotes= 0
CorreyVotes=0
LiVotes = 0
OTooleyVotes=0


import csv
#Open CSV files
with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
    #Removing the CSV header
    csv_header= next(csvreader)
   # Putting Candidates votes into list
    for rows in csvreader:
        VoterID.append(rows[0])
        County.append((rows[1]))
        Candidatevotes.append((rows[2]))
#Finding out the unique list of Candidates
for x in Candidatevotes:
    if x not in Candidateslist:
        Candidateslist.append(x)
#print(Candidateslist)
#Counting votes using loops
for x in Candidatevotes:
    if x == "Khan":
        KhanVotes= KhanVotes + 1
    elif x == "Correy":
        CorreyVotes=CorreyVotes + 1
    elif x == "Li":
        LiVotes=LiVotes+1
    elif x == "O'Tooley":
        OTooleyVotes=OTooleyVotes+1

#print(KhanVotes)
#print(CorreyVotes)
#print(LiVotes)
#print(OTooleyVotes)
Total_Votes= KhanVotes + LiVotes + OTooleyVotes + CorreyVotes
Total_Vote=[KhanVotes,CorreyVotes,LiVotes,OTooleyVotes]
max_votes = max(Total_Vote)
#print(Total_Votes)

#Printing the results
print("Election Results")
print("-----------------------------------")
print(f"Total votes:  {Total_Votes}")
print("----------------------------------")
print(f"{Candidateslist[0]}: {round((float(KhanVotes)/float(Total_Votes)*100),4)} ({KhanVotes}) ")
print(f"{Candidateslist[1]}: {round((float(CorreyVotes)/float(Total_Votes)*100),4)} ({CorreyVotes}) ")
print(f"{Candidateslist[2]}: {round((float(LiVotes)/float(Total_Votes)*100),4)} ({LiVotes}) ")
print(f"{Candidateslist[3]}: {round((float(OTooleyVotes)/float(Total_Votes)*100),4)} ({OTooleyVotes}) ")
print("----------------------------------")
print(f"Winner: {Candidateslist[Total_Vote.index(max_votes)]}")
print("----------------------------------")

