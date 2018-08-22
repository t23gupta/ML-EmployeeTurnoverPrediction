import csv
import os
import datetime

def date_to_year(date):
    if date != '':
        return int((date.split("/")[-1]).split(" ")[0])

csvfile = open('GeoffData.csv', 'r')
readCSV = csv.reader(csvfile, delimiter=',')

today = datetime.datetime.now()
tyear = today.year

# Get a list of all columns from the CSV
csv_col_list = next(readCSV)
csv_col_list[1] = 'Age'
csv_col_list[9] = 'Tenure'
del csv_col_list[10]

newfile = open('Model4.csv', 'w', newline='')
csvwriter = csv.writer(newfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

csvwriter.writerow(csv_col_list)

for row in readCSV:
    
    if row == csv_col_list:
            continue
    else:
        
# =============================================================================
#         # Skip all students/interns/co-ops because we always know they're going to leave
#         if row[2] == "Student" or row[2] == "Intern" or row[2] == "Co-Op":
#             continue
#         if row[4] == "Student":
#             continue
# =============================================================================
        
        # Only want permanent full time employees, skip over all others
        if row[2] != "Permanent Full Time":
            continue
        elif row[4] == "Student" or row[4] == "Intern" or row[4] == "Co-Op":
            continue
        
        #row[4] is Job Title
        # Segregating job titles into broad categories
        if "Superintendent" in row[4]:
            row[4] = "Superintendent"
        elif "Coord" in row[4]:
            row[4] = "Coordinator"
        elif "Manager" in row[4]:
            row[4] = "Manager"
        elif "Admin" in row[4]:
            row[4] = "Admin"
        elif "Dir," in row[4] or "Director" in row[4]:
            row[4] = "Director"
        elif "Analyst" in row[4]:
            row[4] = "Analyst"
        elif "Specialist" in row[4]:
            row[4] = "Specialist"
        elif "VP" in row[4] or "Vice President" in row[4]:
            row[4] = "VP"
        elif "Account" in row[4]:
            row[4] = "Accounting"
        elif "Develop" in row[4]:
            row[4] = "Developer"
        elif "Design" in row[4]:
            row[4] = "Design"
        elif "Control" in row[4]:
            row[4] = "Controller"
        elif "Estimator" in row[4]:
            row[4] = "Estimator"
        elif "Field Engineer" in row[4]:
            row[4] = "Field Engineer"
        elif "Supervisor" in row[4]:
            row[4] = "Supervisor"
        elif "Reception" in row[4]:
            row[4] = "Receptionist"
        else:
            row[4] = "Other"
        
        
        birth_date = str(row[1]) 
        seniority_date = str(row[9])
        termination_date = str(row[10])
        
        # Convert dates into years
        if birth_date != '':
            byear = int((birth_date.split("/")[-1]).split(" ")[0])

        if termination_date != '':
            tyear = int((termination_date.split("/")[-1]).split(" ")[0])
        
        if seniority_date != '':
            syear = int((seniority_date.split("/")[-1]).split(" ")[0])
        
        age = tyear - byear
        tenure = tyear - syear
        
        row[1] = age
        if tenure < 0:
            row[9] = None
        else:
            row[9] = tenure
        
        del row[10]
       
        csvwriter.writerow(row)
        age = None
        tenure = None
        
        
