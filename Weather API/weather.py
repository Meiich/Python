import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_city():
    name = input("Enter city name: ")
    return name


def get_weather(city):
    

    api_key = "2a66447393896a63060292271777ec9c"
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
    return response.json()

def show_weather(data):
    print("City: ", data["name"])
    print("temperature: ", data["main"]["temp"], "°C")
    print("Description: ", data["weather"][0]["description"])
    print("Humidity: ", data["main"]["humidity"], " %")

def main():
    name = get_city()
    data = get_weather(name)
    show_weather(data)

main()
