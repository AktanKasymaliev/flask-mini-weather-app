import requests
from datetime import datetime

from weather.decorators import city404
from weather import app 
from weather.urls import urlpatterns
from configurations.configuration import load_conf

from flask import render_template, request

@app.route(urlpatterns['main_page'], methods=['GET', 'POST'])
@city404
def get():
    url = "http://api.openweathermap.org/data/2.5/weather?q="
    if request.args.get("city"):
        cityname = request.args.get("city").title()
        response = requests.get(url+cityname+'&appid='+load_conf("API", "key")).json()
        cel = response['main']['temp_max'] - 273.15
        fr = cel*9/5+32
        city = response['name']
        country = response['sys']['country']
        feel = response['main']['feels_like'] - 273.15
        wind_speed = response['wind']['speed']
        weather = response['weather'][0]['description']
        pressure = response['main']['pressure']
        humidity = response['main']['humidity']
        visibility = response['visibility']
        context = {
                "cityname": True,
                "cel": round(float(cel)),
                "date": datetime.now().date(),
                "fr": fr,
                "city": city,
                "country": country,
                "feel": round(float(feel)),
                "wind_speed": wind_speed,
                "weather": weather.title(),
                "pressure": pressure,
                "humidity": humidity,
                "visibility": visibility
            }
        return render_template("weather.html", context=context)
    else:
        context = {
                'date': datetime.now().date(),
                "cityname": False,
                'cel':'NA-/',
                'country':'NA-/',
                "city": 'NA-/',
                'fahrenheit':'NA-/',
                'feel':'NA-/',
                'wind_speed':'NA-/',
                'weather':'NA-/',
                'pressure':'NA-/',
                'humidity':'NA-/',
                'visibility':'NA-/'}
        return render_template("weather.html", context=context)
