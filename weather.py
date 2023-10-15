import tkinter as tk
import ttkbootstrap as ttk
import requests

API = 'oXM6iRR0BuYWOBPluABaiMnsp2ANyZFo'
URL = 'http://dataservice.accuweather.com/'

def weather():
    city = entry_var.get()
    city = city.capitalize()
    label_city_info_var.set(city)
    response_location = requests.get(f'{URL}locations/v1/cities/search', params={"apikey": API, 'q': city})
    if response_location.status_code == 200:
        data_location = response_location.json()
        if data_location:
            location_key = data_location[0]['Key']
            response = requests.get(f"{URL}currentconditions/v1/{location_key}", params={'apikey':API, 'details': 'true'})
            print(response.text)
            print("")
            if response.status_code == 200:
                data = response.json()
                if data:
                    weather_details=data[0]
                    weather = weather_details['WeatherText']
                    label_weather_info_var.set(weather)
                    temp = weather_details['Temperature']['Metric']['Value']
                    label_temp_info_var.set(temp)
                    humidity = weather_details['RelativeHumidity']
                    label_humidity_info_var.set(humidity)
                    wind_speed = weather_details['Wind']['Speed']['Metric']['Value']
                    label_wind_info_var.set(wind_speed)
                    pressure = weather_details['Pressure']['Metric']['Value']
                    label_pressure_info_var.set(pressure)
                    


window = ttk.Window(themename='darkly')

window.title("Duckulator")
window.geometry('500x600')
window['background']='#061c40'

frame_one = tk.Frame(window)
frame_one.configure(bg='#061c40')

label_name = tk.Label(frame_one, text='Weather')
label_name.pack(pady=20)
label_name.config(bg='#061c40',font=("Arial", 20), fg='#ededed')

entry_var = tk.StringVar()
entry = tk.Entry(frame_one, font=("Arial", 20), textvariable=entry_var, width=10)
entry['background'] = '#bdbdbd'
entry.pack(pady=15)

frame_one.pack()

frame_two = tk.Frame(window)
frame_two.configure(bg='#061c40')

frame_two.columnconfigure((0,1), weight=1)
frame_two.rowconfigure((0,1,2,3,4,5,6), weight=1)

#miasto

label_city_name=tk.Label(frame_two, text="City:")
label_city_name.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_city_name.grid(column=0, row=0, sticky='nsew')

label_city_info_var = tk.StringVar()
label_city_info=tk.Label(frame_two, text="", textvariable=label_city_info_var)
label_city_info.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_city_info.grid(column=1, row=0, sticky='nsew')

#pogoda

label_weather_name=tk.Label(frame_two, text="Weather:")
label_weather_name.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_weather_name.grid(column=0, row=1, sticky='nsew')

label_weather_info_var = tk.StringVar()
label_weather_info=tk.Label(frame_two, text="", textvariable=label_weather_info_var)
label_weather_info.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_weather_info.grid(column=1, row=1, sticky='nsew')
frame_two.pack()

#temperatura

label_temp_name=tk.Label(frame_two, text="Temperature:")
label_temp_name.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_temp_name.grid(column=0, row=2, sticky='nsew')

label_temp_info_var = tk.StringVar()
label_temp_info=tk.Label(frame_two, text="", textvariable=label_temp_info_var)
label_temp_info.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_temp_info.grid(column=1, row=2, sticky='nsew')


#humidity


label_humidity_name=tk.Label(frame_two, text="Humidity:")
label_humidity_name.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_humidity_name.grid(column=0, row=3, sticky='nsew')

label_humidity_info_var = tk.StringVar()
label_humidity_info=tk.Label(frame_two, text="", textvariable=label_humidity_info_var)
label_humidity_info.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_humidity_info.grid(column=1, row=3, sticky='nsew')
frame_two.pack()

#pressure

label_pressure_name=tk.Label(frame_two, text="Pressure:")
label_pressure_name.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_pressure_name.grid(column=0, row=4, sticky='nsew')

label_pressure_info_var = tk.StringVar()
label_pressure_info=tk.Label(frame_two, text="", textvariable=label_pressure_info_var)
label_pressure_info.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_pressure_info.grid(column=1, row=4, sticky='nsew')
frame_two.pack()

#prędkośc wiatru

label_wind_name=tk.Label(frame_two, text="Wind speed:")
label_wind_name.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_wind_name.grid(column=0, row=5, sticky='nsew')

label_wind_info_var = tk.StringVar()
label_wind_info=tk.Label(frame_two, text="", textvariable=label_wind_info_var)
label_wind_info.config(bg='#061c40',font=("Arial", 16), fg='#ededed')
label_wind_info.grid(column=1, row=5, sticky='nsew')
frame_two.pack()

button = ttk.Button(window, text="Find", padding=6 , fs=10, command=weather)
button.pack(pady=20)


window.mainloop()