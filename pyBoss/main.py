# In this challenge, you get to be the boss. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

# Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:

# Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:
# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
# 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
import csv
import os


f = open("raw_data/employee_data1.csv")
reader = csv.DictReader(f)
data = [row for row in reader]

g = open("raw_data/employee_data2.csv")
reader2 = csv.DictReader(g)
data2 = [row for row in reader2]

# Specify the file to write to
output_path = os.path.join('output', 'new.csv')

#Create Variables
#ids
empId = []
#names
names = []
nameCollider = []
seperateNames = []
firstName = []
lastName =[]
#DOB
dob = []
years = []
months = []
days = []
newDobs = []
#SSN
#State
#for loop to go through the first csv 
for row in data:
	#then append each id to the empId list
	empId.append(row["Emp ID"])
#for loop to go throught the second csv
for row in data2:
	#and append each id to the empId list
	empId.append(row["Emp ID"])
#check to make sure that both are printing	
#print("Emp Id: " + str(empId))
#It works! empId is now a list of all the employee ids. now We need to add it to the first row of our new csv.

# Then convert and export the data to use the following format instead:
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL
# 15,Samantha,Lara,09/08/1993,***-**-7526,CO
# 411,Stacy,Charles,12/20/1957,***-**-8526,PA
# In summary, the required conversions are as follows:

# The Name column should be split into separate First Name and Last Name columns.
#grab the names and put them in the name list
for row in data:
	names.append(row["Name"])
for row in data2:
	names.append(row["Name"])
#print(names)
#convert the names list to a string so we can split each name
nameCollider = " ".join(str(e) for e in names)
#print(nameCollider)
#split the seperated names
seperateNames = nameCollider.split(" ")
#move the first names to their list
firstName = seperateNames[::2]
#move the last names to their list
lastName = seperateNames[1::2]
    #do something
#print(firstName)
#print(lastName)

# The DOB data should be re-written into DD/MM/YYYY format.
#grab all the DOBs
for row in data:
	dob.append(row["DOB"])
for row in data2:
	dob.append(row["DOB"])

#now, from this 1985-12-04 to this 12/04/1985
#print(dob)
dobCollider = " ".join(str(e) for e in dob)
#print(dobCollider)
seperateDob = dobCollider.replace('-', ' ').split(' ')
print(seperateDob)

years = seperateDob[::3] 
months = seperateDob[1::3]
days = seperateDob[2::3]
#print(years)
#print(months)
#print(days)
i = 0
while i < len(years):
	newDobs.append(months[i] + "/" + days[i] + "/" + years[i])
	i = i+1
print(newDobs)
#Succ motha fuckin cess!!!!


# The SSN data should be re-written such that the first five numbers are hidden from view.


#
# The State data should be re-written as simple two-letter abbreviations.


#Use this for writing reference
#Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    # # Write the first row (column headers)
    # csvwriter.writerow(['First Name', 'Last Name', 'SSN'])
    
    # # Write the second row
    # csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])

