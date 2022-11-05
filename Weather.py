import requests

api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid=033511f1161ec331a3c53e4b02444913'
weather = requests.get(api_address).json()

def temp():
    temparature = round(weather["main"]["temp"]-273.1)
    return temparature

def des():
    description = weather["weather"][0]["description"]
    return description