import pyowm
import pytz
from datetime import datetime
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
obs = mgr.weather_at_place('Boston, US')
weather = obs.weather

# Write your code here
