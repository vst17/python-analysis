# we are importing the OS module
import os
import csv
import sys

# os.path to create a path to connect to the csv files

PyBank_Data = os.path.join('..','PyBank', 'budget_data_1.csv') 
# variables to track 
Total_Months = 0
Total_Revenue = 0.0
Greatest_Inc = -sys.maxsize - 1
Greatest_Inc_Date = ""
Greatest_Decrease = sys.maxsize 
Greatest_Decrease_date = ""

#method 1 to read the file
with open(PyBank_Data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
# looping through all rows to count the months, total revenue , find greatest increase, decrease in revenue
    for row in csvreader:
        Total_Months +=1 
        Total_Revenue += float(row[1].strip())
        if int(row[1]) >= Greatest_Inc:
            Greatest_Inc = int(row[1])
            Greatest_Inc_Date = row[0]
        if int(row[1]) <= Greatest_Decrease:
            Greatest_Decrease = int(row[1])
            Greatest_Decrease_date = row[0]

# to calculate the average revenue change

Average_Change = round(Total_Revenue/Total_Months,2)

# results

print("Financial Analysis")
print("--------------------------------")
print("Total Months: " + str(Total_Months))
print("Total Revenue: $" + str(Total_Revenue))
print("Average Revenue Change: $" + str(Average_Change))
print("Greatest Increase in Revenue: " + Greatest_Inc_Date + " ($" + str(Greatest_Inc) + ")")
print("Greatest Decrease in Revenue: " + Greatest_Decrease_date + "")

# creating a new file for our results
new_PyBank = open("output.txt", "w")

# writing results

new_PyBank.write("Financial Analysis")
new_PyBank.write( ":" + "\n")
new_PyBank.write("Total Months: " + str(Total_Months) + "\n")
new_PyBank.write("Total Revenue: " + str(Total_Revenue) + "\n")
new_PyBank.write("Average Revenue Change: $" + str(Average_Change) + "\n")
new_PyBank.write("Greatest Increase in Revenue: " + Greatest_Inc_Date + " ($" + str(Greatest_Inc) + ")" + "\n")
new_PyBank.write("Greatest Decrease in Revenue: " + Greatest_Decrease_date + " ($" + str(Greatest_Decrease) + ")" + "\n")





    



    