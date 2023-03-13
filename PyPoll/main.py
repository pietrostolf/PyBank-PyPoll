#import dependencies
import os
import csv

#declare vote variables
votes_charles = 0
votes_diana = 0        
votes_raymon = 0
votecount = 0

#path for csv file
budget_csv = os.path.join("Resources","election_data.csv")

#open csv file
with open(budget_csv, 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)  
    header = next(csvreader)

#iterate through csv rows to find votes counts   
    for row in csvreader:
        votecount +=1
        if row[2] == "Charles Casper Stockham":
            votes_charles += 1
        elif  row[2] == "Diana DeGette": 
            votes_diana += 1
        elif  row[2] == "Raymon Anthony Doane": 
            votes_raymon += 1
        
#asociate each vote counte with its respective candidate   
vote_dic = {"Charles Casper Stockham": votes_charles, "Diana DeGette": votes_diana, "Raymon Anthony Doane": votes_raymon}           

#display results on the console
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {votecount}")
print("-----------------------------------")
print(f"Charles Casper Stockham: {round((votes_charles/votecount)*100,3)}% ({votes_charles})")
print(f"Diana DeGette: {round((votes_diana/votecount)*100,3)}% ({votes_diana})")
print(f"Raymon Anthony Doane: {round((votes_raymon/votecount)*100,3)}% ({votes_raymon})")
print("-----------------------------------")
print(f"Winner: {max(vote_dic, key=lambda k: vote_dic[k])}")
print("-----------------------------------")

#generate txt file with results
with open('analysis/output.txt', 'w') as f:
        f.write("Election Results\n")
        f.write("-----------------------------------\n")
        f.write(f"Total Votes: {votecount}\n")
        f.write("-----------------------------------\n")
        f.write(f"Charles Casper Stockham: {round((votes_charles/votecount)*100,3)}% ({votes_charles})\n")
        f.write(f"Diana DeGette: {round((votes_diana/votecount)*100,3)}% ({votes_diana})\n")
        f.write(f"Raymon Anthony Doane: {round((votes_raymon/votecount)*100,3)}% ({votes_raymon})\n")
        f.write("-----------------------------------\n")
        f.write(f"Winner: {max(vote_dic, key=lambda k: vote_dic[k])}\n")
        f.write("-----------------------------------\n")
    