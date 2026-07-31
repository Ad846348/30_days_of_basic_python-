import requests

API_KEY = "b299b7d00fb8471e3db694b6b7984606"

def get_weather():
    city = input("Enter City Name: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"]!= 200:
            print("City nahi mili")
            return

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        print("\n--- Weather Report ---")
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Weather: {weather}")
        print(f"Humidity: {humidity}%")

    except:
        print("Internet check karo ya API key galat hai")

get_weather()
