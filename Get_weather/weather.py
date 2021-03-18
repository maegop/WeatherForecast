import pyowm
from api_key import API_KEY
import pytz
import datetime

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('Madrid, ES')
weather = obs.weather

temperature = weather.temperature(unit='celsius')['temp']
humidity = weather.humidity
wind = weather.wind('miles_hour')['speed']
clouds = weather.clouds

# Weather status
print(f'Today\'s weather in Madrid: {weather.status}')
print(f'Today\'s weather: {weather.detailed_status}')

# print(weather.temperature())
print(f'The current cloud coverage for Madrid is {clouds}%')
print(f'The current wind speed for Madrid is {wind} mph')
print(f'The current humidity is {humidity}%')
print(f'The temperature in Madrid is {temperature} degrees Celsius.')

# Sunrise and Sunset times
sunrise = weather.sunrise_time(timeformat='iso')
sunset = weather.sunset_time(timeformat='iso')

print(f'The sunrise for Madrid is {sunrise}')
print(f'The sunset for Madrid is {sunset}')
