# Weather API Docs

## Steps to Run the API

### 1. Clone this Repo.

### 2. Get your own API key.
Go to https://openweathermap.org/api and create an account. One you sign in go to your API keys. Copy that key and paste it in the `api_key` section of the `sample-config.py` file. Create a .gitignore file and type your config file there - this is so that your API key if kept secret and not pushed to your github.

### 3. Get Weather information
At the bottom of the `weather_api.py` file there is a `summary` function:

```
  def summary():
     Location = getAirportLoc('AES') #put in airport iata code
     City = getCity(Location) #gets airport city
     Summary = getWeatherSummary(City) #gets weather from that city
     return Summary
```

Edit the string in the `getAirportLoc` function to your desired airport IOTA code.

### 4. Running the code
To run the code navigate to the code directory and type `python weather_api.py` Text on the terminal should appear as the following:

```
* Serving Flask app "weather_api" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 438-135-100
```   
### 5.  Accessing the data
While the code is running, in your browser fo to `http://127.0.0.1:5000/summary` A JSON of a weather summary of the airport location you inputted should appear.
