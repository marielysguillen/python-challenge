import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv") #find csv file 

#--------------------------------------------
# Variable Declaration
#---------------------------------------------
months_total = 1        #months printing
profit_loss_total = 0   #profit/loss total printing
current_value = 0       #row value
average_pl = 0          #average change
row1 = 0                #gets the first line after the header
greatest_increase = 0
greatest_decrease = 0
greatest_increase_period = ""
greatest_decrease_period = ""
profit_months_list = [] #save period
profit_losses_list = [] #save profit/losses changes

#--------------------------------------------
# Open and read csv
#---------------------------------------------
with open(budget_data_csv) as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    row1 = next(csv_reader)  # gets the first line 

    #Set current value and profit loss total with the first line (column B) -> 1088983
    current_value = int(row1[1]) 
    profit_loss_total = int(row1[1])
    
    # Read through the rest of the data
    for row in csv_reader:

        # Add the total number of months included in the dataset
        months_total = months_total + 1

        # Add the net total amount of "Profit/Losses" over the entire period
        profit_loss_total = int(profit_loss_total) + int(row[1])

        # Add month data into a list for the average change
        profit_months_list.append(row)

        # Changes in "Profit/Losses" over the entire period
        profit_change = int(row[1])-current_value 
        profit_losses_list.append(profit_change)
        current_value = int(row[1])
        #print(profit_change)
        #print(current_value)

        # Add average of those changes
        average_pl = sum(profit_losses_list)/len(profit_losses_list)
        average_pl = round(average_pl,2) #round 2 decimals

        #Calculate the greatest increase/decrease based on averagre change and months data
        if greatest_increase < profit_change:
            greatest_increase = profit_change
            greatest_increase_period = profit_months_list[-1][0] #Get last element in this profit_months_list for column A         

        if greatest_decrease > profit_change:
            greatest_decrease = profit_change
            greatest_decrease_period = profit_months_list[-1][0] #Get last element in this profit_months_list for column A         

#--------------------------------------------
# Output
#---------------------------------------------
print("Financial Analysis")
print("----------------------------")

# The total number of months included in the dataset
print("Total Months:", months_total)

# The net total amount of "Profit/Losses" over the entire period
print("Total:",'$' + str(profit_loss_total))

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
print("Average Change:",'$' + str(average_pl))

# The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: " + greatest_increase_period + " " + "($" + str(greatest_increase) + ")" )

# The greatest decrease in profits (date and amount) over the entire period
print("Greatest Decrease in Profits: " + greatest_decrease_period + " " + "($" + str(greatest_decrease) + ")" )

#--------------------------------------------
# Export a text file with the results.
#---------------------------------------------
pyBank_analysis = os.path.join("Analysis", "pyBank_analysis.txt")
with open(pyBank_analysis,"w") as file:

    file.write("Financial Analysis")
    file.write("\n" + '----------------------------' + '\n')
    file.write( 'Total Months: ' + str(months_total) + '\n' )
    file.write( 'Total: $' + str(profit_loss_total) + '\n' )
    file.write( 'Average Change: $' + str(average_pl) + '\n' )
    file.write( 'Greatest Increase in Profits:' + ' ' + str(greatest_increase_period) + '($' + repr(greatest_increase) + ')' + '\n' )
    file.write( 'Greatest Decrease in Profits:' + ' ' + str(greatest_decrease_period) + '($' + repr(greatest_decrease) + ')' )  