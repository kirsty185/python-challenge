import os
import csv
file = os.path.join('budget_data.csv') #open csv file at this path
with open('budget_data.csv', 'r')as csv_file: #open and read csv file
    csvreader = csv.reader(csv_file, delimiter=',') 
    header = next(csvreader) #first row is a header
    month_count = [] #empty list
    profit = []
    change_profit = []

    for row in csvreader: #loop through rows and add to the empty list
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1): #assign index
        change_profit.append(profit[i+1]-profit[i]) # calculation to work out difference in profit between months

increase = max(change_profit) #set maximum value in list
decrease = min(change_profit) #set minimum value in list

month_increase = change_profit.index(max(change_profit))+1 # to run through each row
month_decrease = change_profit.index(min(change_profit))+1
        
#print the table displayed in Module 3 challenge. I used W3schools as I did not know how to do this.
print("Financial Analysis")
print("------------------------------------------------")
print(f"Total Months:{len(month_count)}") #f string, count of the month_count variable created minus the header row declared row 6, 7
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}") #average change in profit from column 2,  new value - old value/ old value
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")

#write a text file in the analysis folder #I used w3schools for this as I had no idea how to do it
output = os.path.join('python-challenge','PyBank','Analysis')
output = open("txtfile.txt", "w")
output.write("Financial Analysis\n")#stackover flow says \n will create a new line 
output.write("------------------------------------------------\n")
output.write(f"Total Months:{len(month_count)}\n") #f string, count of the month_count variable created minus the header row declared row 6, 7
output.write(f"Total: ${sum(profit)}\n")
output.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}\n") #average change in profit from column 2,  new value - old value/ old value
output.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})\n")
output.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})\n")
