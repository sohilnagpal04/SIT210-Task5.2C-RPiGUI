from tkinter import *
import tkinter.font
from turtle import width
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
 
redled = LED(14)
greenled = LED(15)
blueled = LED(18)

win = Tk()
win.title("LED Toggler")
win.geometry("570x200")
myFont = tkinter.font. Font(family = 'Helvetica', size = 12 )

def ledRED():
    if redled.is_lit:
        redled.off()
        ledButton1["text"] = "RED"
    else:
        redled.on()
        ledButton1["text"] = "LED off"
      
def ledGREEN():
    if greenled.is_lit:
        greenled.off()
        ledButton2["text"] = "GREEN"
    else:
        greenled.on()
        ledButton2["text"] = "LED off"
         
def ledBLUE():
    if blueled.is_lit:
        blueled.off()
        ledButton3["text"] = "BLUE"
    else:
        blueled.on()
        ledButton3["text"] = "LED off"
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
    

var = IntVar()


ledButton1 = Radiobutton(win, text = "RED",indicatoron = 0,value=1, font = myFont,command =ledRED, bg = 'red',variable=var, width =20, height =5)
ledButton1.grid (row=1, column=1)
 
ledButton2 = Radiobutton(win, text = "GREEN",bg = 'green',indicatoron = 0,value=2, font = myFont,command = ledGREEN,variable=var, width =20, height =5)
ledButton2.grid (row=1, column=2)

ledButton3 = Radiobutton(win, text = "BLUE",bg = 'blue',indicatoron = 0,value=3, font = myFont,command = ledBLUE,variable=var,  width =20, height =5)
ledButton3.grid (row=1, column=3)

ledButton4 = Button(win, text = "EXIT", font = myFont,command = close, width =15, height =4)
ledButton4.grid (row=2, column=2)
