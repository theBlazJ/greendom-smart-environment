#vstavimo potrebne knjižice in module 

import RPi.GPIO as GPIO       	 
import time 

 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(7,GPIO.OUT) 

 
from tkinter import* 
myGui=Tk() 

 
#definira funkciji za izklapljanje in vklapljanje črpalk 
def vklop_crpalke(): 
    GPIO.output(7,True) 
def izklop_crpalke(): 
    GPIO.output(7,False) 

 

#napis in resolucija rezultata 
myGui.title("Nadzorovanje črpalke") 
myGui.geometry("200x350") 

 
while True: 

    gumb1=Button(text='on',fg='black',bg='green',command=vklop_crpalke).pack() 
    gumb2=Button(text='off',fg='black',bg='green',command=izklop_crpalke).pack() 
    myGui.mainloop() 