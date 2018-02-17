#Don't forget to import csv!
import csv

#This is what I'm aiming for:
#Expected Output Result 
# Financial Analysis
# ----------------------------
# Total Months: 25
# Total Revenue: $1241412
# Average Revenue Change: $216825
# Greatest Increase in Revenue: Sep-16 ($815531)
# Greatest Decrease in Revenue: Aug-12 ($-652794)

# f = open("budget_data_1.csv")
# reader = csv.DictReader(f)
# for row in reader:
#   # Add your own logic here
#   # ...for example, printing out data in the column "Name" for each row would be:
#   print(row["Date"])

f = open("raw_data/budget_data_1.csv")
reader = csv.DictReader(f)
# data = [row for row in reader]

dates = []
revenues = []
totalRevenue = 0
avgChange = []


g = open("raw_data/budget_data_2.csv")
reader2 = csv.DictReader(g)
data2 = [row for row in reader2]


print("Financial Analysis")
print("---------------------------")

#Total Months
#To find total months, I want to loop through the data set, and append each date to a new list
#called dates. Then we just need to print the length of the dates array to find the total number
#of months in our csv. Remember we have to change the interger that length returns to a string
#so that it will print.

#for loop to go through the csv 
for row in reader:
	#then append each month to the dates list
	dates.append((row["Date"]))
#nicely formatted total months
print("Total Months: " + str(len(dates)))



#Total Revenue
#To find the total revenue, I need to loop through the data, and append each revenue item to
#a new list called revenues. Then I need to convert the strings in the revenues list to integers
#so that I can do addition. And then we set the sum of revenues equal to a variable, and print
#our results to the console.

#for loop to go through the csv
for row in reader:
	#then append each revenue to the revenues list
	revenues.append((row["Revenue"]))
#convert revenues from strings to integers
revenues = [ int(x) for x in revenues ]
#sum the contents of revenues
totalRevenue = sum(revenues)
#nicely formatted total revenues
print("Total Revenue: " + str(totalRevenue))

#So if I have revenues, which is a list in order of what each month's revenue is, then what I
#need to do is loop through that list, and subtract the previous value from the current value.
#Adding each of these to a list called avgChange. Then I sum the contents of avgChange
#and divide that by the length of the list. This will provide us with the average change.
#Average Change
#for loop to go through the csv
for i in range(1,len(revenues)):
	#subtract the previous number from the current and append it to avgChange
    avgChange.append((revenues[i] - revenues[i-1]))
#print avg of change by dividing the sum of change by the length
print("Average Revenue Change: " + str(sum(avgChange) / (len(avgChange)+1)))



#The greatest increase in revenue (date and amount) over the entire period.
#using the list avgChange, we can find the index of the maximum value.
maxI = avgChange.index(max(avgChange))
#then grab the corresponding date from the same index out of the dates list.
maxChangeDate = dates[maxI]
#then print out our statement to the console.
print("Greatest Increase in Revenue: " + str(maxChangeDate) + "    " + str(max(avgChange)))



#The greatest decrease in revenue (date and amount) over the entire period
#using the list avgChange, we can find the index of the minimum value
minI = avgChange.index(min(avgChange))
#then grab the corresponding date from the same index out of the dates list.
minChangeDate = dates[minI]
#then print out our statement to the console.
print("Greatest Decrease in Revenue: " + str(minChangeDate) + "    " + str(min(avgChange)))