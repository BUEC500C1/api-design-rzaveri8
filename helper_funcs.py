
import csv
import sys
import requests
import pytemperature

def getAirportLoc(code):
    check = isinstance(code,str)
    while check == False:
        return "ERROR: Not a String"
        break
    mycode = code
    with open('airport-codes.csv', 'r') as f:
        rows = list(csv.reader(f))
        csv_file_reader = csv.DictReader(f)
        for i in range(1,3592): #this goes through all of the rows
            for j in range(0,2): #checks each colomn
                if mycode == rows[i][j]:
                    loc = str(rows[i][j-1])
                    #print "thisi is LOc" , loc
                    return loc
            else:
                return "Airport Code not found, please try again"

#parsing out just the city
def getCity(loc):
    check = isinstance(loc,str)
    while check == False:
        return "ERROR: Not a String"
        break
    my_string = loc
    result = [x.strip() for x in my_string.split(',')]
    city = result[0]
    #print city
    return city
#this = getAirportLoc('AES')
#print this
