#!/usr/bin/python
#TO DO
#INPUT CHECKS
#CHECK IF VALID ISO CODE
#CHECK IF STRING

import csv
import sys

def getAirportLoc(code):
    code = code
    with open('airport-codes.csv', 'rb') as f:
        rows = list(csv.reader(f))
        csv_file_reader = csv.DictReader(f)
        for i in range(1,3592):
            for j in range(0,2):
                if code == rows[i][j]:
                    loc = rows[i][j-1]
                    print rows[i][j-1]
    return loc

getAirportLoc('AES')
