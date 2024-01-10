import os
import csv


election_data_csv = os.path.join("Resources", "election_data.csv") #find csv file 

#--------------------------------------------
# Variable Declaration
#---------------------------------------------

total_votes_cast = 0
w = 0
winner_election = ""

# Lists/Dictionaries to store data
candidate_list = []
candidate_votes_dict = {}
candidate_percent_dict = {}
printing_dict = {}
winner_election = ""

#--------------------------------------------
# Open and read csv
#---------------------------------------------
with open(election_data_csv) as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:
       
       #The total number of votes cast
        total_votes_cast = total_votes_cast + 1
        # total_votes_list.append(row[0])

        #Add candidate 
        #Create a dictionary where key is the candidate and item value is the number of votes for that candidate
        #candidate_list.append(row[2])
        c_name = row[2]
        if c_name in candidate_list:
            #Increase count votes for the current candidate
            flag = True
            candidate_votes_dict[c_name] = candidate_votes_dict[c_name] + 1 
            #print('exist')
        else:       
            flag = False
            #Add candidate to the candidate_list
            candidate_list.append(c_name) 
            #Add first vote found for the candidate
            candidate_votes_dict[c_name] = 1
            
# Calculate the percentage of votes each candidate won to 3 decimal places, convert to string later and add "$" for printing
for key, item in candidate_votes_dict.items():
    # votes_count.append(value)
    votes = candidate_votes_dict[c_name]
    # Determine pocent to 3 decimal places
    percent = round((int(item)/ total_votes_cast * 100),3)
    candidate_percent_dict[key] = percent

    #Set winner by comparing the number of votes for each candidate
    if (item > w):
        w = item
        winner_election = key

#--------------------------------------------
# Output
#---------------------------------------------
print("Election Results")
print("-------------------------")
print("Total Votes:" + "" + str(total_votes_cast))
print("-------------------------")

#Zip all two dictionary together and iterate over votes and percent dictionaries at once 
for (key1,item1), (key2,item2) in zip(candidate_votes_dict.items(), candidate_percent_dict.items()):
    # printing_dict[key1] = item1, item2
    print(key1 + ":" + " " + str(item2)+"%" + " " + "(" + str(item1) + ")")

print("-------------------------")
print("Winner:" + " " + winner_election)
print("-------------------------")

#--------------------------------------------
# Export a text file with the results.
#---------------------------------------------
pyPoll_analysis = os.path.join("Analysis", "pyPoll_analysis.txt")
with open(pyPoll_analysis,"w") as file:

    file.write("Election Results")
    file.write("\n" + '-------------------------' + '\n')
    file.write("Total Votes:" + "" + str(total_votes_cast) + '\n')
    file.write('-------------------------' + '\n')

    #Zip all two dictionary together and iterate over votes and percent dictionaries at once 
    for (key1,item1), (key2,item2) in zip(candidate_votes_dict.items(), candidate_percent_dict.items()):
        # printing_dict[key1] = item1, item2
        file.write(key1 + ':' + ' ' + str(item2)+'%' + ' ' + '(' + str(item1) + ')' + '\n' )

    file.write('-------------------------' + '\n')
    file.write('Winner' + ' ' + winner_election + '\n')
    file.write('-------------------------')

    