import os

csvpath= os.path.join("..","Resources","budget_data.csv")
PL=[]
Date=[]
import csv
#Opening the CSV File
with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ',')
#Removing the Header Row    
    csv_header= next(csvreader)
   # Creating a list of Dates and Profit/Lost
    for rows in csvreader:
        Date.append(rows[0])
        PL.append(int(rows[1]))

#Getting the monthly change in Profits 
Changes=0
Changes_PL =[]
for x in range(len(Date)):
    if x ==0:
        Changes=Changes
    elif x>0:
        Changes=PL[x]-PL[x-1]
    Changes_PL.append(Changes)

#Statistics for the change in net income
max_value = max(Changes_PL)
min_value= min(Changes_PL)
avg_value= round(sum(Changes_PL)/int(len(Changes_PL)-1),2)


#Creating a Max Profit (Wanted to Practice more loops lol)
MaxProfits=0 
for x in range(len(Date)):
    MaxProfits = MaxProfits + PL[x]
    

 #Printing the results   
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {len(Date)}")
print(f"Total: {MaxProfits}")
print(f"Average Change: ${avg_value}")
print(f"Greatest Increase in Profits: {Date[Changes_PL.index(max_value)]} (${max_value})")
print(f"Greatest Decrease in Profits: {Date[Changes_PL.index(min_value)]} (${min_value})")
   
   

