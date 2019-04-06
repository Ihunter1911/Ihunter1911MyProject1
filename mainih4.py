
# Import os module 
import os
# Import module for reading CSV files
import csv
# Open and read the csv file. Establish the first row as the header
with open ("budget_data.csv", 'r') as csvfile:
    next(csvfile)
    readcsv = csv.reader(csvfile, delimiter = ",")
    header= next(readcsv)
    num_lines= 0
    total = 0
    PLAverage= 0
    PLHighest= 0
    PLLowest= 0
    HighDate= ' '
    LowDate= ''
    for column in readcsv:
# Sum of the total number of months in the datafile
        num_lines += 1
# Diff (net) total "profit/losses"
        total += int(column[1])
# (Python Conditionals) If ... else statement used to determine if it is the greatest increase in profits has occurred.
# If not, check if the greatest decrease in losses has occured
# If either condition is met, put the value into the variable with the value of the month

    if int(column[1]) > PLHighest:
        PLHighest = int(column[1])
        HighDate = str(column[0])
    elif int(column [1]) < PLLowest:
        PLLowest = int(column[1])
        LowDate = str(column[0])
# Write csv
f = open("budget_results.txt", "w")
f.write("budget info\n")

PLAverage = "{:.2f}".format((total/num_lines))
print("Number of Months: " + str(num_lines))
f.write("Number of Months: " + str(num_lines)+" \n")

print ("Total Profit or Loss: " + str(total))
f.write ("Total Profit or Loss: " + str(total)+" \n")
print ("Average Profit/Loss " + str(PLAverage))
f.write ("Average Profit/Loss " + str(PLAverage)+"\n")
print("Highest Increase " + HighDate + " " + str(PLHighest))
f.write("Highest Increase " + HighDate + " " + str(PLHighest)+" \n")
print ("Highest Decrease " + LowDate + " " + str(PLLowest))
f.write ("Highest Decrease " + LowDate + " " + str(PLLowest)+" \n")
