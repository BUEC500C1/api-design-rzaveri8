#!/usr/bin/python
#TO DO
#INPUT CHECKS
#CHECK IF VALID ISO CODE
#CHECK IF STRING

import csv
import sys
"""
#input number you want to search
code = raw_input('Enter number to find\n')

#read csv, and split on "," the line
csv_file = csv.reader(open('airport-codes.csv', "rb"), delimiter=",")


#loop through csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if code == row[1][1]:
         print row
"""

#row_number, column_number = [int(arg, 10)-1 for arg in sys.argv[2:])]
code = raw_input('Enter number to find\n')
with open('airport-codes.csv', 'rb') as f:
    rows = list(csv.reader(f))
    csv_file_reader = csv.DictReader(f)
    for i in range(1,3592):
        for j in range(0,2):
            if code == rows[i][j]:
                print rows[i][j-1]



#!/usr/bin/python
#TO DO
#INPUT CHECKS
#CHECK IF VALID ISO CODE
#CHECK IF STRING
"""
3592
1
#input number you want to search
code = raw_input('Enter number to find\n')

with open('airport-codes.csv', 'r') as _filehandler:
    csv_file_reader = csv.DictReader(_filehandler)
    for row in csv_file_reader:
        if code == # Do something here
        print(row['quote'])
        print(row['speaker'])



#loop through csv list
for row in csv_file:
    #if current rows 2nd value is equal to input, print that row
    if code == row[i][j]:
         print row


#row_number, column_number = [int(arg, 10)-1 for arg in sys.argv[2:])]

with open('airport-codes.csv', 'rb') as csvfile:
    readCsv = csv.reader(csvfile,delimiter=',')


     rows = list(csv.reader(f))
        for rows in csv_file
            if code ==


        for row in readCsv:
         for x in range(0,7):
             n+=1
             sensorData.append(float(row[x]))
             """
