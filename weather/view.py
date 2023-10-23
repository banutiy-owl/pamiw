from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime, timedelta
from viewmodel import *

window = tk.Tk()

window.title("Weather")
window.geometry('900x500')
window['background']='#57adff'
window.resizable(False, False)

def buttonClick(e):
    configureDays()

    setCurrentConditions()
    list_days = getDays(input_field.get())
    setDays(list_days)
    setImages(list_days)

    

#clock
clock_var=tk.StringVar()
clock = Label(window, textvariable=clock_var, font=("Helvetica", 30, 'bold'), fg = 'white', bg="#57adff")
clock.place(x=30, y=20)

img = Image.open("search_box.png")
img = img.resize((400,60))
photoImg =  ImageTk.PhotoImage(img)
box_image = tk.Label(window, image=photoImg,  bg = "#57adff")
box_image.place(x=270, y=120)

entry_var = tk.StringVar()
input_field = tk.Entry(window, justify = 'center', textvariable=entry_var, width=16, font=('poppins', 22, 'bold'), bg = '#2166a9', border = 0, fg = 'white')
input_field.place(x=330, y=130)


Label(window, bg="#10477a", width=33, height=10).place(x=30, y=110)

#window
label_temp = Label(window, text="Temperature", font=('Helvetica', 11), fg='white', bg="#10477a")
label_temp.place(x=50, y=125)

label_hum = Label(window, text="Humidity", font=('Helvetica', 11), fg='white', bg="#10477a")
label_hum.place(x=50, y=150)

label_pres = Label(window, text="Pressure", font=('Helvetica', 11), fg='white', bg="#10477a")
label_pres.place(x=50, y=175)

label_wind = Label(window, text="Wind Speed", font=('Helvetica', 11), fg='white', bg="#10477a")
label_wind.place(x=50, y=200)

label_desc = Label(window, text="Description", font=('Helvetica', 11), fg='white', bg="#10477a")
label_desc.place(x=50, y=225)



#api_window

temp_variable=tk.StringVar()
label_temp = Label(window, textvariable=temp_variable, font=('Helvetica', 11), fg='white', bg="#10477a")
label_temp.place(x=150, y=125)

hum_variable=tk.StringVar()
label_hum = Label(window, textvariable=hum_variable, font=('Helvetica', 11), fg='white', bg="#10477a")
label_hum.place(x=150, y=150)

pres_variable=tk.StringVar()
label_pres = Label(window, textvariable=pres_variable, font=('Helvetica', 11), fg='white', bg="#10477a")
label_pres.place(x=150, y=175)

wind_variable=tk.StringVar()
label_wind = Label(window, textvariable=wind_variable, font=('Helvetica', 11), fg='white', bg="#10477a")
label_wind.place(x=150, y=200)

desc_variable=tk.StringVar()
label_desc = Label(window, textvariable=desc_variable, font=('Helvetica', 11), fg='white', bg="#10477a")
label_desc.place(x=150, y=225)




#bottom
frame = Frame(window, width=900, height=180, bg="#2166a9")
frame.pack(side=BOTTOM)


img = Image.open("rectangle.png")
img = img.resize((250,135))
photoImg1 =  ImageTk.PhotoImage(img)
Label(frame, image=photoImg1, bg="#2166a9").place(x=30, y=20)

img = img.resize((120,120))
photoImg2 =  ImageTk.PhotoImage(img)
Label(frame, image=photoImg2, bg="#2166a9").place(x=300, y=30)
Label(frame, image=photoImg2, bg="#2166a9").place(x=450, y=30)
Label(frame, image=photoImg2, bg="#2166a9").place(x=600, y=30)
Label(frame, image=photoImg2, bg="#2166a9").place(x=750, y=30)



#first_main_cell
first_frame = Frame(window, width = 225, height = 118, bg='#10477a')
first_frame.place(x=45, y=350)
day1 = Label(first_frame, font="arial 20", bg="#10477a", fg="#fff")
day1.place(x=100, y=5)

first_image = Label(first_frame, bg="#10477a")
first_image.place(x=10, y=16)

day1_temp_var=tk.StringVar()
day1temp = Label(first_frame, font="arial 12", bg="#10477a", fg="#fff", textvariable=day1_temp_var)
day1temp.place(x=100, y=50)

#second_cell
second_frame = Frame(window, width = 100, height = 100, bg='#10477a')
second_frame.place(x=310, y=360)

day2 = Label(second_frame, font="arial 12", bg="#10477a", fg="#fff")
day2.place(x=10, y=4)

second_image = Label(second_frame, bg="#10477a")
second_image.place(x=20, y=30)

day2_temp_var=tk.StringVar()
day2temp = Label(second_frame, bg="#10477a", fg="#fff", textvariable=day2_temp_var)
day2temp.place(x=10, y=63)


#third_cell
third_frame = Frame(window, width = 100, height = 100, bg='#10477a')
third_frame.place(x=460, y=360)

day3 = Label(third_frame, font="arial 12", bg="#10477a", fg="#fff")
day3.place(x=10, y=4)

third_image = Label(third_frame, bg="#10477a")
third_image.place(x=20, y=30)

day3_temp_var=tk.StringVar()
day3temp = Label(third_frame, bg="#10477a", fg="#fff", textvariable=day3_temp_var)
day3temp.place(x=10, y=63)


#fourth_cell
fourth_frame = Frame(window, width = 100, height = 100, bg='#10477a')
fourth_frame.place(x=610, y=360)

day4 = Label(fourth_frame, font="arial 12", bg="#10477a", fg="#fff")
day4.place(x=10, y=4)

fourth_image = Label(fourth_frame, bg="#10477a")
fourth_image.place(x=20, y=30)

day4_temp_var=tk.StringVar()
day4temp = Label(fourth_frame, bg="#10477a", fg="#fff", textvariable=day4_temp_var)
day4temp.place(x=10, y=63)


#five_cell
five_frame = Frame(window, width = 100, height = 100, bg='#10477a')
five_frame.place(x=760, y=360)

day5 = Label(five_frame, font="arial 12", bg="#10477a", fg="#fff")
day5.place(x=10, y=4)

five_image = Label(five_frame, bg="#10477a")
five_image.place(x=20, y=30)

day5_temp_var=tk.StringVar()
day5temp = Label(five_frame, bg="#10477a", fg="#fff", textvariable=day5_temp_var)
day5temp.place(x=10, y=63)

img4 = Image.open("circle.png")
img4 = img4.resize((50,50))
photoImg4 =  ImageTk.PhotoImage(img4)
button_circle = Label(window, image=photoImg4, bg="#57adff", cursor="target")
button_circle.image=photoImg
button_circle.place(x=670, y=120)
button_circle.bind("<Button-1>", buttonClick)


def configureDays():
    day1.config(text=getDay(1))
    day2.config(text=getDay(2))
    day3.config(text=getDay(3))
    day4.config(text=getDay(4))
    day5.config(text=getDay(5))


def setDays(list_days):
    day1_temp_var.set(f'Min:{list_days[0][0]}\n Max:{list_days[0][1]}')
    day2_temp_var.set(f'Min:{list_days[1][0]}\n Max:{list_days[1][1]}')
    day3_temp_var.set(f'Min:{list_days[2][0]}\n Max:{list_days[2][1]}')
    day4_temp_var.set(f'Min:{list_days[3][0]}\n Max:{list_days[3][1]}')
    day5_temp_var.set(f'Min:{list_days[4][0]}\n Max:{list_days[4][1]}')


def setCurrentConditions():
    locc = getCurrentConditions(input_field.get())
    temp_variable.set(f'{locc[0]} °C')
    hum_variable.set(f'{locc[1]} %')
    pres_variable.set(f'{locc[2]} hPa')
    wind_variable.set(f'{locc[3]} m/s')
    desc_variable.set(f'{locc[4]}')
    iso_string_variable = locc[5]
    parsed_time = datetime.fromisoformat(iso_string_variable)
    clock_var.set(parsed_time.time().strftime("%H:%M"))




def setImages(list_days):
    
    img=Image.open(f'icons/{list_days[0][2]}-s.png')
    resized=img.resize((90,58))
    photo1=ImageTk.PhotoImage(resized)
    first_image.config(image=photo1)
    first_image.image=photo1

    img=Image.open(f'icons/{list_days[1][2]}-s.png')
    resized=img.resize((50,30))
    photo2=ImageTk.PhotoImage(resized)
    second_image.config(image=photo2)
    second_image.image=photo2

    img=Image.open(f'icons/{list_days[2][2]}-s.png')
    resized=img.resize((50,30))
    photo3=ImageTk.PhotoImage(resized)
    third_image.config(image=photo3)
    third_image.image=photo3

    img=Image.open(f'icons/{list_days[3][2]}-s.png')
    resized=img.resize((50,30))
    photo4=ImageTk.PhotoImage(resized)
    fourth_image.config(image=photo4)
    fourth_image.image=photo4

    img=Image.open(f'icons/{list_days[4][2]}-s.png')
    resized=img.resize((50,30))
    photo5=ImageTk.PhotoImage(resized)
    five_image.config(image=photo5)
    five_image.image=photo5


window.mainloop()