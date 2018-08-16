import csv
import os
import datetime

csvfile = open('GeoffData.csv', 'r')
readCSV = csv.reader(csvfile, delimiter=',')

today = datetime.datetime.now()
year = today.year
# Get a list of all columns from the CSV
csv_col_list = next(readCSV)
csv_col_list[1] = 'Age'
csv_col_list[9] = 'Tenure'
csv_col_list[10] = None

newfile = open('GeoffDataRefined.csv', 'w')
csvwriter = csv.writer(newfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

csvwriter.writerow(csv_col_list)

for row in readCSV:
    
    if row == csv_col_list:
            continue
    else:
        birth_date = str(row[1]) 
        seniority_date = str(row[9])
        termination_date = row[10]
        
        byear = int((birth_date.split("/")[-1]).split(" ")[0])
        
        if termination_date != '':
            year = int((termination_date.split("/")[-1]).split(" ")[0])
        
        syear = int((seniority_date.split("/")[-1]).split(" ")[0])
        
        age = year - byear
        tenure = year - syear
        
        row[1] = age
        row[9] = tenure
        row[10] = None
        csvwriter.writerow(row)
        
        