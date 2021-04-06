from tkinter import *

class CountDown:
    def __init__(self,root,min,sec):
        # setting the default value as 0
        self.fgStop = False
        self.minute = min
        self.second = sec
        self.clock_Label = Label(root,text="",font=("arial",30),fg="#3cec3c",bg="black")
        self.clock_Label.place(x=480,y=10)

        self.clock_Label.config(text=self.minute + ":" + self.second)

    
    def start(self):
        sec = int(self.second)
        min = int(self.minute)

        if (sec ==0 and min==0):
            self.fgStop = True
            return

        sec -= 1
        if (sec<0):
            sec=59
            min -= 1

        self.second = str(sec).zfill(2)
        self.minute = str(min).zfill(2)
        self.clock_Label.config(text=self.minute + ":" + self.second)
        if (not self.fgStop):
            self.clock_Label.after(1000,self.start)

