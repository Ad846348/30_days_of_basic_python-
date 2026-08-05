import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "Your_api_key" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Error", "City ka naam likho")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data['main']['temp']
            feels = data['main']['feels_like']
            humidity = data['main']['humidity']
            desc = data['weather'][0]['description'].title()
            wind = data['wind']['speed']

            result = f"City: {city.title()}\n\n"
            result += f"Temp: {temp}°C\n"
            result += f"Feels like: {feels}°C\n"
            result += f"Weather: {desc}\n"
            result += f"Humidity: {humidity}%\n"
            result += f"Wind: {wind} m/s"

            result_label.config(text=result)
        else:
            result_label.config(text="City nahi mili 😢\nSpelling check karo")

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Internet nahi chal raha")
    except:
        messagebox.showerror("Error", "Kuch galat ho gaya")

root = tk.Tk()
root.title("Day 32 - Weather App")
root.geometry("350x300")
root.resizable(False, False)
tk.Label(root, text="Live Weather App", font=("Arial", 16, "bold")).pack(pady=10)
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

tk.Label(input_frame, text="City:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
city_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
city_entry.pack(side=tk.LEFT, padx=5)
city_entry.bind('<Return>', lambda e: get_weather())

tk.Button(root, text="Get Weather", command=get_weather, bg="#2196F3", fg="white",
          font=("Arial", 11, "bold"), width=15).pack(pady=10)


result_label = tk.Label(root, text="City likhke 'Get Weather' dabao",
                        font=("Arial", 11), justify=tk.LEFT, fg="#333")
result_label.pack(pady=15)

root.mainloop()
