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

with open('airport-codes.csv', 'rb') as f:
     rows = list(csv.reader(f))
     print rows[1][0]
