import os
import csv
import operator

totalcount = 0
kcount = 0
ccount = 0
lcount = 0
ocount = 0
max_votecount= 0
def percentage(part,whole):
    return 100*float(part)/float(whole)
# Read in the CSV file
with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        voterid = row[0]
        country = row[1]
        candidate = row[2]
        totalcount = totalcount + 1
        if candidate == "Khan": 
            kcount = kcount + 1
        if candidate =="Correy":
            ccount = ccount + 1
        if candidate == "Li":
            lcount = lcount + 1
        if candidate == "O'Tooley":
            ocount = ocount + 1
        candidatevote= {"Khan":kcount, "Corry":ccount, "Li":lcount, "O' Tooley":ocount}
        winner = max(candidatevote.items(), key=operator.itemgetter(1))[0]
    print (f'Election Results'+ '\n')
    print (f'-----------------------------')
    print (f' Total Votes: {totalcount}')
    print (f'-----------------------------')
    k_percent = percentage(kcount,totalcount)  
    #print(f'Khan: %(kg).2f' {k_percent}{kcount}')
    print( "Khan: {:.2f}".format(k_percent))
    #print(f'Khan: %(kg).2f' {k_percent}{kcount}')
    # print(f'Khan: {percentage(kcount,totalcount):.3f}% ({kcount})')
    # print(f'Correy: {precentage(kcount,totalcount):.3f}%({ccount})')
    # print(f'Li: {percentage(lcount,totalcount):.3f}%({lcount})')
    # print(f'O\'Tooley: {percentage(ocount,totalcount):.3f}%({ocount})')
    # print(f'-----------------------------'+'\n')
    # print ('Winner:{winner}'+'\n')    
    print(winner)
    print(totalcount)
    print (candidatevote)

