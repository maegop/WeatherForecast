import pyowm
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('Cologne')
weather = obs.weather

# Write your code here
print(f'Today\'s weather: {weather.status}')
