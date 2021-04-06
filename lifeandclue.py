from tkinter import *

class LifeHandle:
    def __init__(self,root,lifes):
        #create all img for btn letter
        global hr0,hr1,hr2,hr3,hr4
        hr4=PhotoImage(file="hr4.png")
        hr3=PhotoImage(file="hr3.png")
        hr2=PhotoImage(file="hr2.png")
        hr1=PhotoImage(file="hr1.png")
        hr0=PhotoImage(file="hr0.png")

        self.LabelLife1=Label(root,bg="#E7FFFF",image=hr4)
        self.LabelLife1.place(x=0,y=30)
  
        self.LabelLife2=Label(root,bg="#E7FFFF",image=hr4)
        self.LabelLife2.place(x=28,y=30)
        #if lifes[1]==0:
        #    self.LabelLife2.config(image=hr0)

        self.LabelLife3=Label(root,bg="#E7FFFF",image=hr4)
        self.LabelLife3.place(x=56,y=30)
        #if lifes[2]==0:
        #    self.LabelLife3.config(image=hr0)

        self.LabelLife4=Label(root,bg="#E7FFFF",image=hr4)
        self.LabelLife4.place(x=84,y=30)
        #if lifes[3]==0:
        #    self.LabelLife4.config(image=hr0)

        self.LabelLife5=Label(root,bg="#E7FFFF",image=hr4)
        self.LabelLife5.place(x=112,y=30)
        #if lifes[4]==0:
        #    self.LabelLife5.config(image=hr0)
    def updLifes(self,lifes):
        global hr0,hr1,hr2,hr3,hr4
        for i in range(len(lifes)-1,-1,-1):
            if (lifes[i]>0):
                exec('self.LabelLife{}.config(image=hr{})'.format(i+1,lifes[i]))
            else:
                exec('self.LabelLife{}.config(image=hr0)'.format(i+1))
         
    def RemoveLife(self,lifes):
        global hr0,hr1,hr2,hr3,hr4
        for i in range(len(lifes)-1,-1,-1):
            if (lifes[i]>0):
                lifes[i] -= 1
                exec('self.LabelLife{}.config(image=hr{})'.format(i+1,lifes[i]))
                break

class ClueHandle:
    def __init__(self,root,clues):
        #create all img for btn letter
      
        global cl0,cl1
        cl1=PhotoImage(file="cl1.png")
        cl0=PhotoImage(file="cl0.png")

        self.LabelClue1=Label(root,bg="#E7FFFF",image=cl1)
        self.LabelClue1.place(x=0,y=60)
        self.LabelClue2=Label(root,bg="#E7FFFF",image=cl1)
        self.LabelClue2.place(x=28,y=60)
        self.LabelClue3=Label(root,bg="#E7FFFF",image=cl1)
        self.LabelClue3.place(x=56,y=60)
        self.LabelClue4=Label(root,bg="#E7FFFF",image=cl1)
        self.LabelClue4.place(x=84,y=60)
        self.LabelClue5=Label(root,bg="#E7FFFF",image=cl1)
        self.LabelClue5.place(x=112,y=60)

    def updClues(self,clues):
        global cl0,cl1
        for i in range(len(clues)-1,-1,-1):
            if (clues[i]>0):
                exec('self.LabelClue{}.config(image=cl{})'.format(i+1,clues[i]))
            else:
                exec('self.LabelClue{}.config(image=cl0)'.format(i+1))
         

    def RemoveClue(self,clues):
        global cl0,cl1
        for i in range(len(clues)-1,-1,-1):
            if (clues[i]>0):
                clues[i] -= 1
                exec('self.LabelClue{}.config(image=cl{})'.format(i+1,clues[i]))
                break
