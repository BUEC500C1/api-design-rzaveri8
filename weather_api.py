#!/usr/bin/python
#TO DO
#CONVERT TEMP FROM KELVIn to FARENHEIGHT
"""  build a library/package where I can call your API and pass
it an airport name and you return back to me the weather information
"""

import csv
import sys
import pytemperature
import requets
import flask
import json
from flask import jsonify
import config


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

def getWeatherSummary(city):
    key = config.api_key()
    api_address="http://api.openweathermap.org/data/2.5/weather?" + "appid=" + key + "&q="
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
        return "ERROR: An Http Error occurred:" + repr(errh)
    except requests.exceptions.ConnectionError as errc:
        return "ERROR: An Error Connecting to the API occurred:" + repr(errc)
    except requests.exceptions.Timeout as errt:
        return "ERROR: A Timeout Error occurred:" + repr(errt)
    except requests.exceptions.RequestException as err:
        return "ERROR: An Unknown Error occurred" + repr(err)
    try:
        data = response['main']
    except KeyError:
        return "ERROR: City not found, please try again"
    except NameError:
        return "ERROR:: Not a string"
    try:
        formatted_data = response['weather'][0]['description']
    except KeyError:
        return "ERROR: City not found, please try again"
    except NameError:
        return "ERROR:: Not a string"

    temp = data['temp']
    temp = pytemperature.k2f(temp) # Kelvin to Fahrenheit
    humidity = data['humidity']
    humidity = humidity
    #humidity =
    feels_like = data['feels_like']
    feels_like = pytemperature.k2f(feels_like)# Kelvin to Fahrenheit

    summary = [

        {
        'Description': formatted_data,
        'Outside Temperature': temp,
        'Humidity': humidity,
        'Feels like': feels_like}
    ]
    return summary




app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/summary', methods=['GET'])
def summary():
    Location = getAirportLoc('AES') #put in airport iata code
    City = getCity(Location) #gets airport city
    Summary = getWeatherSummary(City) #gets weather from that city
    #print Summary
    main = [{'Location': Location, 'Weather': Summary }]
    return jsonify(main)


app.run()
