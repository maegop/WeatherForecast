import pyowm
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
forecaster = mgr.forecast_at_place('Los Angeles, US', '3h')

# Write your code here
