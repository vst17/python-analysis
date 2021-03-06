# import operating system and csv
import os
import csv

# setting the path
csvpath = os.path.join('Resources', 'employee_data2.csv')


# tracking variables
emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

# creating a dictionary of states and abbreviations
us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
    'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',
    'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY',
}

# reading the file in
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    # looping through the read file
    for row in csvreader:
        # appending employee id to a new list
        emp_id.append(row[0])

        # appending first & last name to two separate lists
        # splitting name by space
        # appending first name
        # appending last name    
        name = row[1].split(" ") 
        first_name.append(name[0]) 
        last_name.append(name[1]) 

        # formatting & appending dob mm/dd/yyyy
        # splitting dob by '-'
        # formatting dob
        # appending formatted dob
        # appending formatted dob
        bdate = row[2].split("-") 
        new_db = bdate[1] + "/" + bdate[2] + "/" + bdate[0] 
        dob.append(new_db) 

        #formatting & appending ssn
        # splitting ssn by '-'
        # formatting ssn
        # appending formatted ssn
        ssn_split = row[3].split("-") 
        new_ssn = "***-**-" +ssn_split[2]
        ssn.append(new_ssn) 

        # looping through states dictionary
        state.append(us_state_abbrev[row[4]])

# tests
# print(first_name[0])
# print(last_name[0])
# print(dob[0])
# print(ssn[0])
# print(state[0])

# zipping data
employees = zip(emp_id, first_name, last_name, dob, ssn, state)

# creting the new csv file
output_file = os.path.join('Output/employee_data_clean_2.csv')

# opening & writing the file
with open(output_file, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')

    # writing in headers
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # writing data
    for employee in employees:
        writer.writerow(employee)





