import tkinter as tk
import requests
from tkinter import font

HEIGHT = 600
WIDTH = 600


def get_weather(city):
    weather_key = 'YOUR_API_KEY'
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature(C): %s' % (
            name, desc, temp)

    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


root = tk.Tk()
root.title("WEATHER APP")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='lightblue', bd=5)  # bd is border
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 15))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=(
    'Courier'), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='lightblue', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 15))
label.place(relwidth=1, relheight=1)

root.mainloop()
