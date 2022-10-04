from turtle import width
from tkinter import *
from tkinter import ttk
from tkinter import font
from cgitb import text
from PIL import ImageTk, Image
import requests
import json

#colors
co1 = "white"
co2= "#333333"
co3 = "#000000"

#configure the windows for the tracker
window = Tk()
window.title('')
window.geometry('320x350')
window.configure(bg=co1)


#-------------------------------------------------------------------------------
def info():
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=USD%2CEUR%2C%2CCAD"
    r = requests.get(api_link)
    dic = r.json()

    #USD
    usd_value = float(dic["USD"])
    print(usd_value)
    usd_formatted_value = "$ {:,.3f}".format(usd_value)
    usd ["text"] = usd_formatted_value

    #Euros
    euros_value = float(dic["EUR"])
    print(usd_value)
    euros_formatted_value = "{:,.3f}".format(euros_value)
    euros["text"] = "Europe : € " +euros_formatted_value

    #CAD
    cad_value = float(dic["CAD"])
    print(cad_value)
    cad_formatted_value = "{:,.3f}".format(cad_value)
    cad ["text"] = "Canada : CAD " + cad_formatted_value

    frame_body.after(1000,info)


#-------------------------------------------------------------------------------------------------


frame_head = Frame(window, width =320, height =50,bg =co1)
frame_head.grid(row=1,column=0)

frame_body = Frame(window, width =320, height =300,bg =co2)
frame_body.grid(row=2,column=0)

image_1 = Image.open('images/solana.png')
image_1 = image_1.resize((30,30))
image_1 = ImageTk.PhotoImage(image_1)

icon_1 = Label(frame_head, image = image_1, bg = co1)
icon_1.place(x=10, y =10)

name = Label(frame_head, text ="Solana Price Tracker", 
            fg = co3,
            padx = 0, 
            width = 17, 
            height = 1,
            anchor = "center",
            font ='Poppins 15')
name.place(x = 50 , y = 10)

usd = Label(frame_body, text="$0000",
            width = 14 , 
            height = 1,
            font = ("Arial 30 bold"),
            bg =co2,
            fg = co1,
            anchor= "center")
usd.place (x=0 , y =29)

euros = Label(frame_body, text="$0000",
            height = 1,
            font = ("Arial 16 bold"),
            bg =co2,
            fg = co1,
            anchor= "center")
euros.place (x=10 , y =130)

cad = Label(frame_body, text="$0000",
            height = 1,
            font = ("Arial 16 bold"),
            bg =co2,
            fg = co1,
            anchor= "center")
cad.place (x=10 , y =170)

info()

window.mainloop()

