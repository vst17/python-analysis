# import operating system and csv
import os
import csv

# setting the path
PyBosspath = os.path.join('Resources', 'employee_data1.csv')


# tracking variables
employee_id = []
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
with open(PyBosspath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    # looping through the read file
    for row in csvreader:
        # appending employee id to a new list
        employee_id.append(row[0])

        # appending first & last name to two separate lists
        # splitting name by space
        name = row[1].split(" ") 
        # appending first name and appending last name    
        first_name.append(name[0]) 
        last_name.append(name[1]) 

        # formatting & appending dob mm/dd/yyyy
        # splitting dob by '-'
        bdate = row[2].split("-") 
        # formatting dob
        new_db = bdate[1] + "/" + bdate[2] + "/" + bdate[0]
        # appending formatted dob
        dob.append(new_db) 

        #formatting & appending ssn
        # splitting ssn by '-'
        ssn_split = row[3].split("-") 
        # formatting ssn
        # appending formatted ssn
        new_ssn = "***-**-" +ssn_split[2]
        ssn.append(new_ssn) 

        # looping through states dictionary
        state.append(us_state_abbrev[row[4]])



# zipping data
employees = zip(employee_id, first_name, last_name, dob, ssn, state)

# creting the new csv file
output_boss = os.path.join('Output/employee_data_clean_1.csv')

# opening & writing the file
with open(output_boss, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')

    # writing in headers
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # writing data
    for employee in employees:
        writer.writerow(employee)





