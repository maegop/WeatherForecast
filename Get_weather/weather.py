import pyowm
from *.api_key import API_KEY
import pytz
import datetime

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('Boston, US')
weather = obs.weather
temperature = weather.temperature(unit='fahrenheit')['temp']
humidity = weather.humidity
wind = weather.wind('miles_hour')['speed']
clouds = weather.clouds

print(f'Today\'s weather: {weather.status}')
print(f'Today\'s weather: {weather.detailed_status}')
print(weather.temperature())
print(f'The current humidity is {humidity}%')
print(
    f'The temperature in San Francisco, California is {temperature} degrees Fahrenheit.')
print(f'The current cloud coverage for Los Angeles, California is {clouds}%')
print(f'The current wind speed for Los Angeles, California is {wind}mph')

# Sunrise and Sunset times
print(weather.sunrise_time(timeformat='iso'))
print(weather.sunset_time(timeformat='iso'))
