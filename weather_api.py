#!/usr/bin/python
#TO DO
#INPUT CHECKS
#CHECK IF VALID ISO CODE
#CHECK IF STRING

import csv
import sys
import requests


def getAirportLoc(code):
    check = isinstance(code,str)
    while check == False:
        return "ERROR: Not a String"
        break
    mycode = code
    with open('airport-codes.csv', 'rb') as f:
        rows = list(csv.reader(f))
        csv_file_reader = csv.DictReader(f)
        for i in range(1,3592): #this goes through all of the rows
            for j in range(0,2): #checks each colomn
                if mycode == rows[i][j]:
                    loc = str(rows[i][j-1])
                    print rows[i][j-1]
    return loc

def getWeather(loc):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=b1a9759151e09b557fb47fa074cd751e&q='
    city = loc
    try:
        url = api_address + city
    except TypeError:
        return "Error: Not a string"
        #return

#below is my error checking for the API.
    try:
        response = requests.get(url).json()
    except requests.exceptions.HTTPError as errh:
        print "An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        print "An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        print "A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        print "An Unknown Error occurred" + repr(err)
    except NameError:
        print "NAME ERROR"
        return
    try:
        formatted_data = response['weather'][0]['description']
    except KeyError:
        return "City not found, please try again"
    except NameError:
        print "Error: Not a string"
        return

#print(formatted_data)
getWeather('adsfsdfdsfs')
#getAirportLoc()
