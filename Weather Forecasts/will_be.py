import pyowm
from pyowm.utils import timestamps
from datetime import timedelta, datetime
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()

#checks if there is rain in this week's forecast for LA
forecaster = mgr.forecast_at_place('Los Angeles, US', '3h')

# Write your code here
print(forecaster.will_have_rain())
print(forecaster.will_have_clouds())

#The date specified must be a date that is included in the five day forecast. If the date is not in the forecast it will cause an error.
print(forecaster.will_be_stormy_at(datetime(2021, 3, 16, 12, 0)))

print(forecaster.will_be_foggy_at(timestamps.tomorrow()))

"""
will_have_rain()
will_have_clear()
will_have_fog()
will_have_clouds()
will_have_snow()
will_have_storm()
will_have_tornado()
will_have_hurricane()
"""

"""
will_be_rainy_at()
will_be_clear_at()
will_be_foggy_at()
will_be_cloudy_at()
will_be_snowy_at()
will_be_stormy_at()
will_be_tornado_at()
will_be_hurricane_at()
"""

"""
Use timestamps.tomorrow() as explained in the Get Weather At a Specific Time step to complete the following instructions.
"""
