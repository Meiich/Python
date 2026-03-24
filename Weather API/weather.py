import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_city():
    name = input("Enter city name: ")
    return name


def get_weather(city):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    )
    return response.json()


def show_weather(data):
    if data.get("cod") != 200:
        print("Error:", data.get("message", "Something went wrong"))
        return

    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Description:", data["weather"][0]["description"])
    print("Humidity:", data["main"]["humidity"], "%")


def main():
    city = get_city()
    data = get_weather(city)
    show_weather(data)


if __name__ == "__main__":
    main()