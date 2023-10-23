import requests
API = 'PjxxH7Gnc4fh4rSmPsG5VaOhwyFUAnwn'
URL = 'http://dataservice.accuweather.com/'

def current_conditions(city):
    location_key = getLocationKey(city)
    response = requests.get(f"{URL}currentconditions/v1/{location_key}", params={'apikey':API, 'details': 'true'})
    if response.status_code == 200:
        data = response.json()
        if data:
            weather_details=data[0]
            weather = weather_details['WeatherText']
            temp = weather_details['Temperature']['Metric']['Value']
            humidity = weather_details['RelativeHumidity']
            wind_speed = weather_details['Wind']['Speed']['Metric']['Value']
            pressure = weather_details['Pressure']['Metric']['Value']
            time = weather_details['LocalObservationDateTime']
            list_return = [temp, humidity, pressure, wind_speed, weather, time]
            return list_return

def getLocationKey(city):
    city = city.capitalize()
    response_location = requests.get(f'{URL}locations/v1/cities/search', params={"apikey": API, 'q': city})
    if response_location.status_code == 200:
        data_location = response_location.json()
        if data_location:
            return data_location[0]['Key']


def forDay(num, city):
    response = requests.get(f"{URL}forecasts/v1/daily/5day/{getLocationKey(city)}", params={'apikey' : API, 'metric': 'true'})
    if response.status_code == 200:
        data = response.json()
        if 'DailyForecasts' in data:
            daily_forecast = data['DailyForecasts'][num-1] 
            min_temp = daily_forecast['Temperature']['Minimum']['Value']
            max_temp = daily_forecast['Temperature']['Maximum']['Value']
            day_icon = daily_forecast['Day']['Icon']
            list_response=[min_temp, max_temp, day_icon]
            return list_response

