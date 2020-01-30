#!/usr/bin/python
#TO DO
#CONVERT TEMP FROM KELVIn to FARENHEIGHT

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

def getWeatherDescription(city):
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=b1a9759151e09b557fb47fa074cd751e&q='
    city = city
    try:
        url = api_address + city
    except TypeError:
        #print "Error: Not a string"
        return "ERROR: Not a string"
        #return

#below is my error checking for the API.
    try:
        response = requests.get(url).json()
    except requests.exceptions.HTTPError as errh:
        print "ERROR: An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        print "ERROR: An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        print "ERROR: A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        print "ERROR: An Unknown Error occurred" + repr(err)
    try:
        formatted_data = response['weather'][0]['description']
    except KeyError:
        return "ERROR: City not found, please try again"
    except NameError:
        return "ERROR:: Not a string"
    return formatted_data

tryCode = getAirportLoc('AES')
print 'this is try location:',tryCode
tryCity = getCity(tryCode)
print 'this is try city:',tryCity
tryWeather = getWeatherDescription(tryCity)
print 'this is try weather:',tryWeather
