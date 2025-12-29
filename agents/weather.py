import requests
import json

cord_url = "https://geocoding-api.open-meteo.com/v1/search"
forecast_url = "https://api.open-meteo.com/v1/forecast"

# def get_city_name():
#     city_name = input("Enter the name of the city: ")
#     return city_name

def get_cordinates(name):
    parameters = {
    "name" : name,
    }

    response = requests.get(cord_url, params=parameters)
    r = response.json()

    res = r['results'][0]
    latitude = res['latitude']
    longitude = res['longitude']
    return latitude, longitude


def get_weather_info(name):

    weather_forecast = {}

    name = get_cordinates(name)
    lat, long = name

    parameters = {
            "latitude" : lat,
            "longitude" : long,
            "daily" : "temperature_2m_max"
    }

    response = requests.get(forecast_url, params=parameters)
    r = response.json()
    # print(r)

    days = []
    for time in r["daily"]["time"]:
        days.append(time)
        
    temperature = []
    for temp in r["daily"]["temperature_2m_max"]:
        temperature.append(temp)
        
    for day_info, temp_info in zip(days, temperature):
        weather_forecast[day_info] = temp_info

    return weather_forecast