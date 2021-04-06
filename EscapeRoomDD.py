
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
from sympy import Symbol
from sympy import diff
from sympy import sin,cos,tan,cot
from scipy.misc import derivative
from sympy.utilities.lambdify import lambdify
from math import pi
from random import randint
from tkinter import ttk

import json
from json import JSONEncoder
from functools import partial 
import requests
import random
from time import sleep
import partida as pt
import clockdown as clk
import apidata as api
import lifeandclue as lifeInfo


LARGE_FONT= ("Verdana", 12)





class WrappingLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.bind('<Configure>', lambda e: self.config(wraplength=self.winfo_width()))

class EscapeRoomapp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

 

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, Menu, StartGame, Instructions, Record, Narrativa1, Biblioteca,Hangman,Criptograma,Derivada,Puerta,Logicabool,LabSL001,Adivin,Servidores,Rock,Palabras,NumAleatorio,Saman):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        
        global imagen1
        global imagen2
        global imagen3


        tk.Frame.__init__(self,parent, bg= 'black')
        self.controller = controller
        self.controller.title('Escape Room DD')
        self.controller.geometry('600x400')

        imagen1 =tk.PhotoImage(file ='escape_room_3.png')
        headingLabel1 = tk.Label(self, image = imagen1, bg = 'black').pack()
        
        imagen2 =tk.PhotoImage(file = 'login_button_2.png')
        button = tk.Button(self, image = imagen2, border = 0 , bg = 'black',command=lambda: controller.show_frame(PageOne))
        button.place(x=90, y=190)

        imagen3 =tk.PhotoImage(file ='new_user.png')
        button2 = tk.Button(self, image = imagen3, border = 0, bg= 'black', command=lambda: controller.show_frame(PageTwo))
        button2.place(x=300, y= 190)



class PageOne(tk.Frame):
    

    def __init__(self, parent, controller):

        global imagen5
        global user
        userName = tk.StringVar()  
        pwd = tk.StringVar()  
        

        tk.Frame.__init__(self, parent, bg = 'black')
        self.controller = controller
        self.controller.title('Registration')
        self.controller.geometry('600x400')
        imagen5 =tk.PhotoImage(file ='login.png')
        headingLabel2 = tk.Label(self, image = imagen5, bg = 'black').pack()

        label_0 = tk.Label(self, text = '', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        label_0.pack()

        label_1= tk.Label(self, text = 'Username', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        label_1.pack()

        entry_1 = tk.Entry(self, textvariable=userName,width = 29)
        entry_1.pack()

        label_2 = tk.Label(self, text = 'Password', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        label_2.pack()

        entry_2 = tk.Entry(self, textvariable=pwd, width = 29)
        entry_2.pack()

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.place(x= 80, y = 300)

        button2 = tk.Button(self, text="Login", command= partial(user.Login,controller,Menu,userName,pwd))
        button2.place(x = 200, y =300)

        def show_frame(self, cont):

            frame = self.frames[cont]
            frame.tkraise()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        global imagen4

        
       
        tk.Frame.__init__(self,parent, bg= 'black')
        self.controller = controller
        self.controller.title('Registration')
        self.controller.geometry('600x400')

        userName = tk.StringVar()
        firstName = tk.StringVar()
        lastName = tk.StringVar()
        pwd = tk.StringVar()
        cfm_pwd = tk.StringVar()
        phone = tk.StringVar()
        
        imagen4 =tk.PhotoImage(file ='registration.png')
        headingLabel1 = tk.Label(self, image = imagen4, bg = 'black').pack()

        firstName_label = tk.Label(self, text = 'First Name', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        firstName_label.place(x = 40, y = 80)

        firstName_entry = tk.Entry(self, textvariable = firstName, width = 29)
        firstName_entry.place(x = 60, y = 120)

        lastName_label = tk.Label(self, text = 'Last Name', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        lastName_label.place(x = 40, y = 160)

        lastName_entry = tk.Entry(self, textvariable = lastName, width = 29)
        lastName_entry.place(x = 60, y = 200)

        userName_label= tk.Label(self, text = 'Username', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        userName_label.place(x = 340, y = 80)

        userName_entry = tk.Entry(self, textvariable = userName, width = 29)
        userName_entry.place(x = 360, y = 120)

        pwd_label= tk.Label(self, text = 'Password', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        pwd_label.place(x = 340, y = 160)

        pwd_entry = tk.Entry(self, textvariable = pwd, width = 29)
        pwd_entry.place(x = 360, y = 200)

        cfm_pwd_label = tk.Label(self, text = 'Confirm Password', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        cfm_pwd_label.place(x = 340, y = 240)

        cfm_pwd_entry = tk.Entry(self, textvariable = cfm_pwd,width = 29)
        cfm_pwd_entry.place(x = 360, y = 280)

        

        phone_label = tk.Label(self, text = 'Phone Number', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        phone_label.place(x = 40, y = 240)

        phone_entry = tk.Entry(self, textvariable = phone, width = 29)
        phone_entry.place(x = 60, y = 280)

        label_7 = tk.Label(self, text = 'Avatar', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        label_7.place(x = 0, y = 330)

        list1 = ['Scharifker', 'Eugenio Mendoza', 'Pelusa', 'Gandhi']
        avatar = tk.StringVar()
        droplist = tk.OptionMenu(self, avatar , *list1)
        droplist.config(width = 15)
        avatar.set('Select your Avatar')
        droplist.place(x = 160, y= 330)

        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.place(x=380, y= 330)

        button2 = tk.Button(self, text="Register",command=partial(user.Register,user,firstName,lastName,userName,pwd,cfm_pwd,phone))
        button2.place(x=470, y= 330)   

class Menu(tk.Frame):

    def __init__(self, parent, controller):

        global imagen7
        global imagen8
        global imagen9
        global imagen10
        
        tk.Frame.__init__(self,parent, bg= 'black')
        self.controller = controller
        self.controller.title('Escape Room')
        self.controller.geometry('600x400')

        headingLabel4 = tk.Label(self, text = '', bg = 'black').pack()

        imagen7 =tk.PhotoImage(file ='MainMenu.png')
        headingLabel1 = tk.Label(self, image = imagen7, bg = 'black').pack()

        headingLabel2 = tk.Label(self, text = '', bg = 'black').pack()
        headingLabel3 = tk.Label(self, text = '', bg = 'black').pack()
        
        imagen8 =tk.PhotoImage(file = 'StartGame2.png')
        button = tk.Button(self, image = imagen8, border = 0 , bg = 'black',command=lambda: controller.show_frame(StartGame))
        button.pack()

        imagen9 =tk.PhotoImage(file = 'Instructions2.png')
        button2 = tk.Button(self, image = imagen9, border = 0, bg= 'black', command=lambda: controller.show_frame(Instructions))
        button2.pack()

        imagen10 =tk.PhotoImage(file = 'records2.png')
        button3 = tk.Button(self, image = imagen10, border = 0, bg= 'black', command=lambda: controller.show_frame(Record))
        button3.pack()

class StartGame(tk.Frame):

    def __init__(self, parent, controller):
        
        global imagen11
        global imagen12
        global imagen13
        global imagen14
        global user
        global defaultMin
        tk.Frame.__init__(self,parent, bg= 'black')
        self.controller = controller
        self.controller.title('Escape Room')
        self.controller.geometry('600x400')

        imagen11 =tk.PhotoImage(file ='select1.png')
        headingLabel1 = tk.Label(self, image = imagen11, bg = 'black').pack()

        imagen12 =tk.PhotoImage(file = 'easy1.png')
        button = tk.Button(self, image = imagen12, border = 0 , bg = 'black',command=lambda:self.btnLevelClick(user,1,controller,Narrativa1))
        button.pack()
        imagen13 =tk.PhotoImage(file = 'medium1.png')
        button = tk.Button(self, image = imagen13, border = 0 , bg = 'black',command=lambda:self.btnLevelClick(user,2,controller,Narrativa1))
        button.pack()
        imagen14 =tk.PhotoImage(file = 'hard1.png')
        button = tk.Button(self, image = imagen14, border = 0 , bg = 'black',command=lambda:self.btnLevelClick(user,3,controller,Narrativa1))
        button.pack()

    def btnLevelClick(self,user,level,controller,Narrativa1):
        user.NewPartida(level,defaultMin)
        controller.show_frame(Narrativa1)

class Instructions(tk.Frame):

    def __init__(self, parent, controller):
       
        tk.Frame.__init__(self,parent, bg= 'black')
        self.controller = controller
        self.controller.title('Escape Room')
        self.controller.geometry('600x400')

class Record(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg= 'black')
        self.controller = controller
        self.controller.title('Escape Room')
        self.controller.geometry('600x400')

class Narrativa1(tk.Frame):

    def __init__(self, parent, controller):

        global imagen15
        global imagen16
        global imagen17
        global imagen18
        global user

        tk.Frame.__init__(self,parent, bg= 'black')
        self.controller = controller
        self.controller.title('Escape Room')
        self.controller.geometry('600x400')
       

        imagen15 =tk.PhotoImage(file ='Saman_Narrativa.png')
        headingLabel1 = tk.Label(self, image = imagen15, bg = 'black').place(x=0, y=0, relwidth=1, relheight=1)

        headingaLabel_0 = WrappingLabel(self,text= 'Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que si es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la informacion de SAP de estudiantes, pagos y asignaturas. Necesitamos que nos ayudes a recuperar el disco '+ defaultMin+' minutos, antes de que el servidor se caiga y no se pueda hacer mas nada.',bg="black",fg= 'white',font=("arial",14))
        headingaLabel_0.pack(fill='x')

        imagen16 =tk.PhotoImage(file ='aceptas.png')
        headingLabel6 = tk.Label(self, image = imagen16, bg = 'black').place(x = 120, y = 190)

        imagen17 =tk.PhotoImage(file = 'yes1.png')
        button = tk.Button(self, image = imagen17, bg = 'black', border = 0 ,command=lambda: controller.show_frame(Biblioteca))
        button.place(x = 200, y = 290)

        imagen18 =tk.PhotoImage(file = 'no1.png')
        button = tk.Button(self, image = imagen18,bg = 'black', border = 0,command=lambda: controller.show_frame(Narrativa1))
        button.place(x = 310, y= 290)

class Biblioteca(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg= '#cc9966')
        self.controller = controller
        self.controller.title('Escape Room')
        self.controller.geometry('600x400')

        global imagen19
        global imagen20
        global imagen21
        global imagen22
        global imagen23
        global imagen24
        global imagen25
        global imagen26
        global imagen27

        global user

        headingLabel2 = tk.Label(self, text = '' , bg = '#8c5927', width = 400)
        headingLabel2.pack(side = 'bottom', fill = 'x')

        #mueble de sentarse
        imagen19 =tk.PhotoImage(file ='mueble.png')
        button = tk.Button(self, image = imagen19,bg = '#cc9966', border = 0,command=lambda: controller.show_frame(Derivada))
        button.place(x = 0, y= 260)

        #biblioteca
        imagen20 =tk.PhotoImage(file ='libros.png')
        button = tk.Button(self, image = imagen20,bg = '#cc9966', border = 0,command=lambda: controller.show_frame(Hangman))
        button.place(x = 200, y= 157)

        #mueble con gabetas
        imagen21 =tk.PhotoImage(file ='mueble2.png')
        button = tk.Button(self, image = imagen21, bg = '#cc9966', border = 0,command=lambda: controller.show_frame(Criptograma))
        button.place(x = 412, y= 260)

        imagen22 =tk.PhotoImage(file ='ventana.png')
        headingLabel6 = tk.Label(self, image = imagen22, bg = 'black').place(x = 60, y = 100)

        imagen23 =tk.PhotoImage(file ='ventana1.png')
        headingLabel6 = tk.Label(self, image = imagen23, bg = 'black').place(x = 200, y = 100)

        imagen24 =tk.PhotoImage(file ='ventana2.png')
        headingLabel6 = tk.Label(self, image = imagen24, bg = 'black').place(x = 340, y = 100)

        imagen25 =tk.PhotoImage(file ='ventana3.png')
        headingLabel6 = tk.Label(self, image = imagen25, bg = 'black').place(x = 480, y = 100)

        imagen26 =tk.PhotoImage(file = 'izquerda.png')
        button = tk.Button(self, image = imagen26, bg = '#cc9966', border = 0 ,command=lambda: controller.show_frame(Saman))
        button.place(x = 0, y = 80)

        imagen27 =tk.PhotoImage(file = 'derecha.png')
        button = tk.Button(self, image = imagen27, bg = '#cc9966', border = 0 ,command=lambda: controller.show_frame(Puerta))
        button.place(x = 560, y = 80)
    
    def btnLevelClick(self,controller,frameGame):
        frameGame.startgame(user)
        controller.show_frame(frameGame)
class Hangman(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg= '#E7FFFF')
        self.controller = controller
        self.controller.title('Hangman Game')
        self.controller.geometry('600x400')

        global user
        global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,clImg
        global h1,h2,h3,h4,h5,h6,h7


        self.score = 0
        self.count = 0
        self. win_count = 0

        
        self.g01= api.GameInfo("Biblioteca","ahorcado")
        self.answer = self.g01.answer.lower()
        self.question = self.g01.question
        self.clueMsg = self.g01.clueMsg
       
       
   
   
        self.ckl1=clk.CountDown(self,"00","00")
        #self.ckl1.start()

        #self.lifes=[4,4,4]
        self.lifes=user.lifes
        self.lf=lifeInfo.LifeHandle(self,self.lifes)

        #self.clues=[1,1,1]
        self.clues=user.clues
        self.cl=lifeInfo.ClueHandle(self,self.clues)

        clImg=tk.PhotoImage(file="cluebtn.png")
        btnClue=tk.Button(self,bd=0,command=lambda:self.Hint(),bg="#E7FFFF",activebackground="#E7FFFF",image=clImg)
        btnClue.place(x=2,y=100)

        #btn enter answer
        btn =tk.Button(self,text="Iniciar",command=lambda:self.startgame(user))
        btn.place(x=2,y=150 )

         #place the question label
        label_question = tk.Label(self,text=self.question,bg="#E7FFFF",font=("arial",16))
        label_question.place(x=50,y=300 )
    
        posx = 50    
        #place _ char for echat leter os answer
        for im in range(0,len(self.answer)):
            posx += 40
            exec('self.d{}=tk.Label(self,text="_",bg="#E7FFFF",font=("arial",30))'.format(im))
            exec('self.d{}.place(x={},y={})'.format(im,posx,250))

        #create all img for btn letter
        #al = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        #for let in al:
        #    exec('{}=tk.PhotoImage(file="{}.png")'.format(let,let))
        a =tk.PhotoImage(file ='a.png')
        b =tk.PhotoImage(file ='b.png')
        c =tk.PhotoImage(file ='c.png')
        d =tk.PhotoImage(file ='b.png')
        e =tk.PhotoImage(file ='e.png')
        f =tk.PhotoImage(file ='f.png')
        g =tk.PhotoImage(file ='g.png')
        h =tk.PhotoImage(file ='h.png')
        i =tk.PhotoImage(file ='i.png')
        j =tk.PhotoImage(file ='j.png')
        k =tk.PhotoImage(file ='k.png')
        l =tk.PhotoImage(file ='l.png')
        m =tk.PhotoImage(file ='m.png')
        n =tk.PhotoImage(file ='n.png')
        o =tk.PhotoImage(file ='o.png')
        p =tk.PhotoImage(file ='p.png')
        q =tk.PhotoImage(file ='q.png')
        r =tk.PhotoImage(file ='r.png')
        s =tk.PhotoImage(file ='s.png')
        t =tk.PhotoImage(file ='t.png')
        u =tk.PhotoImage(file ='u.png')
        v =tk.PhotoImage(file ='v.png')
        w =tk.PhotoImage(file ='w.png')
        x =tk.PhotoImage(file ='x.png')
        y =tk.PhotoImage(file ='y.png')
        z =tk.PhotoImage(file ='z.png')

        #create all img for hang man boddy
        h123 = ['h1','h2','h3','h4','h5','h6','h7']
        for hangman in h123:
            exec('{}=tk.PhotoImage(file="{}.png")'.format(hangman,hangman))

        #   list with all place all btn for letter
        button = [['b1','a',0,330],['b2','b',46,330],['b3','c',92,330],['b4','d',138,330],['b5','e',184,330],['b6','f',230,330],['b7','g',276,330],['b8','h',322,330],['b9','i',368,330],['b10','j',414,330],['b11','k',460,330],['b12','l',506,330],['b13','m',552,330],['b14','n',0,360],['b15','o',46,360],['b16','p',92,360],['b17','q',138,360],['b18','r',184,360],['b19','s',230,360],['b20','t',276,360],['b21','u',322,360],['b22','v',368,360],['b23','w',414,360],['b24','x',460,360],['b25','y',506,360],['b26','z',552,360]]

       # b1 = tk.Button(self,bd=0,bg="#E7FFFF",activebackground="#E7FFFF",font=10,image=a)
       # b1.config(command=partial(self.checkletter,'a',b1))
       # b1.place(x = 0, y= 330)
        for q1 in button:
            exec('{}=tk.Button(self,bd=0,bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(q1[0],q1[1]))
            exec('{}.config(command=partial(self.checkletter,"{}",{}))'.format(q1[0],q1[1],q1[0]))
            exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
        
            #hangman placement     command=lambda:self.btnLevelClick(1,controller,Narrativa1)
        #han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h4'],['c5','h5'],['c6','h6'],['c7','h7']]
       # for p1 in han:
        #    exec('label{}=tk.Label(self,bg="#E7FFFF",image=self.{})'.format(p1[0],p1[1]))

        # placement of first hangman image
        h1 =tk.PhotoImage(file ='h1.png')
        self.labelc1 = tk.Label(self, image = h1)

        h2 =tk.PhotoImage(file ='h2.png')
        self.labelc2 = tk.Label(self, image = h2)

        h3 =tk.PhotoImage(file ='h3.png')
        self.labelc3 = tk.Label(self, image = h3)

        h4 =tk.PhotoImage(file ='h4.png')
        self.labelc4 = tk.Label(self, image = h4)

        h5 =tk.PhotoImage(file ='h5.png')
        self.labelc5 = tk.Label(self, image = h5)

        h6 =tk.PhotoImage(file ='h6.png')
        self.labelc6 = tk.Label(self, image = h6)

        h7 =tk.PhotoImage(file ='h7.png')
        self.labelc7 = tk.Label(self, image = h7)

        self.labelc1.place(x = 200,y =- 25)
  
    def startgame(self,user):

        self.score = 0
        self.count = 0
        self. win_count = 0

        

        #self.ckl=clk.CountDown(self,"15","12")
        #self.ckl1=clk.CountDown(self,user.min,user.sec)
        self.ckl1.minute=user.min
        self.ckl1.second=user.sec
        self.ckl1.start()

        self.lifes=user.lifes
        self.lf.updLifes(self.lifes)

        self.clues=user.clues
        self.cl.updClues(self.clues)

        self.labelc1.place(x = 200,y =- 25)

    # button press check function
    def checkletter(self,letter,btn):
        global count
        global win_count
        global score
        global clueCount
        global lifeCount
        global lf
        global lifes 
        global user
       
        btn.destroy()

        #exec('{}.destroy()'.format(btn))
        if letter in self.answer:
            for i in range(0,len( self.answer)):
                if self.answer[i] == letter:
                    self.win_count += 1
                    exec('self.d{}.config(text="{}")'.format(i,letter.upper()))
            if self.win_count == len(self.answer):
                self.score += 1
                answer1 = messagebox.showinfo('GAME OVER','YOU WON!!')
                user.min=self.ckl1.minute
                user.sec=self.ckl1.second
                #self.ckl.fgStop=True
                self.score = 0
                self.count = 0
                self.win_count = 0
                self.labelc2.destroy();
                self.labelc3.destroy();
                self.labelc4.destroy();
                self.labelc5.destroy();
                self.labelc6.destroy();
                self.labelc7.destroy();
                self.controller.show_frame(Biblioteca)
        else:
            self.count += 1
            self.lf.RemoveLife(self.lifes)
            exec('self.labelc{}.destroy()'.format(self.count))
            exec('self.labelc{}.place(x={},y={})'.format(self.count+1,200,-25))
            if self.count == 6:
                answer1 = messagebox.showinfo('GAME OVER','YOU LOST!\nGame OVER')
                user.min=self.ckl1.second
                user.sec=self.ckl1.second
                #self.ckl.fgStop=True
                self.score = 0
                self.count = 0
                self.win_count = 0
                self.labelc2.destroy();
                self.labelc3.destroy();
                self.labelc4.destroy();
                self.labelc5.destroy();
                self.labelc6.destroy();
                self.labelc7.destroy();
                self.controller.show_frame(Biblioteca)
               
    def Hint(self):
        global cl
        global clueMsg
        global clues
        if (len(self.clueMsg)>0):
            messagebox.showinfo('Clue',self.clueMsg[0])
            self.cl.RemoveClue(self.clues)
            del self.clueMsg[0]

class Criptograma(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg= '#E7FFFF')
        self.controller = controller
        self.controller.title('Criptograma')
        self.controller.geometry('600x400')

        global user
       
        self.score = 0
        self.count = 0
        self.win_count = 0
        self.ans_str=StringVar()
        
        g01= api.GameInfo("Biblioteca","Criptograma")
        self.question = g01.question
        self.desplazamiento= g01.desplaz
      
   
        self.ckl1=clk.CountDown(self,"00","00")
        #self.ckl1.start()

        #self.lifes=[4,4,4]
        self.lifes=user.lifes
        self.lf=lifeInfo.LifeHandle(self,self.lifes)

        label_preg = tk.Label(self,text="Decifre el siguiente criptograma:",bg="#E7FFFF",font=("arial",14))
        label_preg.place(x=5,y=100 )

        label_ask = tk.Label(self,text="Your Answer",bg="#E7FFFF",font=("arial",14))
        label_ask.place(x=5,y=200 )

        #ask answer of ecuation
        entry_ans=tk.Entry(self,textvariable = self.ans_str,bg="#E7FFFF",font=("arial",14))
        entry_ans.place(x=150,y=200 )

        #btn enter answer
        btn = tk.Button(self,text="Validate",command=self.btnClick)
        btn.place(x=150,y=250 )

         #btn enter answer
        btn1 =tk.Button(self,text="Iniciar",command=lambda:self.startgame())
        btn1.place(x=150,y=300 )

        #btn enter answer
        btn2 = tk.Button(self,text="Salir",command=lambda: controller.show_frame(Biblioteca))
        btn2.place(x=200,y=300 )

        #calculate cryto
        self.question=self.question.upper()
        self.abc="ABCDEFGHIJKLMNSOPQRSTUVWXYZ"
        self.cifrad=""

        for c in self.question:
            if c in self.abc:
                self.cifrad += self.abc[(self.abc.index(c)+self.desplazamiento)%(len(self.abc))]
            else:
                self.cifrad +=c
        #place the question label
        label_question = tk.Label(self,text=self.cifrad,bg="#E7FFFF",font=("arial",14))
        label_question.place(x=5,y=140 )




    def btnClick(self):
        global question
        global ans_str
        global lf
        global lifes
        global user
        value=self.ans_str.get()
        value=value.upper()
   
        if (value==self.question):
                messagebox.showinfo("Answer Verification","Success Answer...")
        else:
            messagebox.showinfo("Answer Verification","Fail...")
            self.lf.RemoveLife(self.lifes) 
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)

    def startgame(self):
        global user
        self.score = 0
        self.count = 0
        self. win_count = 0


        #self.ckl=clk.CountDown(self,"15","12")
        #self.ckl1=clk.CountDown(self,user.min,user.sec)
        self.ckl1.minute=user.min
        self.ckl1.second=user.sec
        self.ckl1.start()

        self.lifes=user.lifes
        self.lf.updLifes(self.lifes)


class Derivada(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg= '#E7FFFF')
        self.controller = controller
        self.controller.title('Criptograma')
        self.controller.geometry('600x400')

        global user
       
        self.score = 0
        self.count = 0
        self.win_count = 0
        self.ans_str=StringVar()
        
        g01= api.GameInfo("Biblioteca","Preguntas matemáticas")
        self.question = g01.question
      
   
        self.ckl1=clk.CountDown(self,"00","00")
        #self.ckl1.start()

        #self.lifes=[4,4,4]
        self.lifes=user.lifes
        self.lf=lifeInfo.LifeHandle(self,self.lifes)

      

        label_ask = tk.Label(self,text="Your Answer",bg="#E7FFFF",font=("arial",14))
        label_ask.place(x=5,y=150 )

        #ask answer of ecuation
        entry_ans=tk.Entry(self,textvariable = self.ans_str,bg="#E7FFFF",font=("arial",14))
        entry_ans.place(x=150,y=150 )

        #btn enter answer
        btn = tk.Button(self,text="Validate",command=self.btnClick)
        btn.place(x=150,y=200 )

          #btn enter answer
        btn1 =tk.Button(self,text="Iniciar",command=lambda:self.startgame())
        btn1.place(x=150,y=250 )

        #btn enter answer
        btn2 = tk.Button(self,text="Salir",command=lambda: controller.show_frame(Biblioteca))
        btn2.place(x=200,y=250 )




        #place the question label
        label_question = tk.Label(self,text=self.question,bg="#E7FFFF",font=("arial",14))
        label_question.place(x=5,y=100 )

   
        #extract funtions
        res= self.question.rsplit('=',1)
        equation= res[len(res)-1]

        #change to english
        fx=equation.replace('sen','sin')

        #calculate derivate
        x=Symbol('x')
        fx2=diff(fx,x)

        #evalueate on pi
        f1= lambdify(x,fx2)
        self.ans= f1(pi)



        resp=str(self.ans)
        label_resp = tk.Label(self,text=resp,bg="#E7FFFF",font=("arial",14))
        label_resp.place(x=5,y=250 )



    
    def btnClick(self):
        global ans
        global ans_str
        global lf
        global lifes
        value=float(self.ans_str.get())

        if (self.ans>0):
            ans_HiLimit=self.ans*1.1
            ans_LowLimit=self.ans*.9
        else:
            ans_HiLimit=self.ans*0.9
            ans_LowLimit=self.ans*1.1

        if (value>ans_LowLimit and value<ans_HiLimit):
                messagebox.showinfo("Answer Verification","Success Answer...")
        else:
            messagebox.showinfo("Answer Verification","Fail...")
            self.lf.RemoveLife(self.lifes) 
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)

    def startgame(self):
        global user
        self.score = 0
        self.count = 0
        self. win_count = 0


        #self.ckl=clk.CountDown(self,"15","12")
        #self.ckl1=clk.CountDown(self,user.min,user.sec)
        self.ckl1.minute=user.min
        self.ckl1.second=user.sec
        self.ckl1.start()

        self.lifes=user.lifes
        self.lf.updLifes(self.lifes)

class Puerta(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg='#b7a481')
        self.controller = controller
        self.controller.title('Puerta')
        self.controller.geometry('600x400')

        global imagen28
        global imagen29
     
        global user


        imagen28 = tk.PhotoImage(file ='door.png')
        headingLabel1 = tk.Button(self, image = imagen28, border = 0, command=lambda: controller.show_frame(Logicabool),bg = '#b7a481').place(x=105, y = 40)

        imagen29 = tk.PhotoImage(file ='mata1.png')
        headingLabel2 = tk.Label(self, image = imagen29, bg = '#b7a481').place(x=15, y = 100)
        headingLabel2 = tk.Label(self, image = imagen29,bg = '#b7a481').place(x=500, y = 100)

        headingLabel3 = tk.Label(self, text = '',border = 0, bg = '#370617').pack(fill = 'x', side = 'bottom')

class Logicabool(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg= '#E7FFFF')
        self.controller = controller
        self.controller.title('Criptograma')
        self.controller.geometry('600x400')

        global user
       
        self.score = 0
        self.count = 0
        self.win_count = 0
        self.ans_str=StringVar()
        
        self.g01= api.GameInfo("Pasillo Laboratorios ","Lógica Booleana")
        self.question =self.g01.question
        self.answer = self.g01.answer.lower()
      
        self.question_str=StringVar()
   
        self.ckl1=clk.CountDown(self,"00","00")
        #self.ckl1.start()

        #self.lifes=[4,4,4]
        self.lifes=user.lifes
        self.lf=lifeInfo.LifeHandle(self,self.lifes)

        
        label_0 = tk.Label(self,text='',bg="#E7FFFF")
        label_0.pack()

        label_1 = tk.Label(self,text='',bg="#E7FFFF")
        label_1.pack()

        label_2 = tk.Label(self,text='',bg="#E7FFFF")
        label_2.pack()

        label_3 = tk.Label(self,text='',bg="#E7FFFF")
        label_3.pack()

        label_4 = tk.Label(self,text='',bg="#E7FFFF")
        label_4.pack()

        label_9 = tk.Label(self,text='',bg="#E7FFFF")
        label_9.pack()

        self.win = WrappingLabel(self,text=self.question,bg="#E7FFFF",font=("arial",15))
        self.win.pack(fill='x')

        label_5 = tk.Label(self,text='',bg="#E7FFFF")
        label_5.pack()

        label_6 = tk.Label(self,text='',bg="#E7FFFF")
        label_6.pack()

        label_7 = tk.Label(self,text='',bg="#E7FFFF")
        label_7.pack()
    
        self.ans_str=StringVar()
        entry_ans=tk.Entry(self,textvariable = self.ans_str,bg="white",font=("arial",14))
        entry_ans.pack()

        label_8 = tk.Label(self,text='',bg="#E7FFFF")
        label_8.pack()

        btn = tk.Button(self,text="Validate",command=self.btnClick)
        btn.pack()

        btn2 = tk.Button(self,text="Iniciar",command=lambda:self.startgame())
        btn2.pack()

        btn3 = tk.Button(self,text="Salir",command=lambda: controller.show_frame(Puerta))
        btn3.place(x=200,y=300 )

    def btnClick(self):
        global question
        global ans_str
        global lf
        global lifes
        value=self.ans_str.get()
   
        if (value==self.answer):
            messagebox.showinfo("Answer Verification","Success Answer...")
            self.controller.show_frame(LabSL001)
        else:
            messagebox.showinfo("Answer Verification","Fail...")
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)

    def startgame(self):
        global user
        self.score = 0
        self.count = 0
        self. win_count = 0
        


        #self.ckl=clk.CountDown(self,"15","12")
        #self.ckl1=clk.CountDown(self,user.min,user.sec)
        self.ckl1.minute=user.min
        self.ckl1.second=user.sec
        self.ckl1.start()

        self.lifes=user.lifes
        self.lf.updLifes(self.lifes)

class LabSL001(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg='#ddb892')
        self.controller = controller
        self.controller.title('Laboratory...')
        self.controller.geometry('600x400')

        global imagen30
        global imagen31
        global imagen32
        global imagen33
        global imagen34
     
        global user


          
        imagen30 = tk.PhotoImage(file ='pizarra.png')
        headingLabel1 = tk.Button(self, image = imagen30, border = 0, bg = '#ddb892').place(x=150, y = 80)

        imagen31 = tk.PhotoImage(file ='mesa.png')
        headingLabel2 = tk.Label(self, image = imagen31,border = 0, bg = '#ddb892').place(x=10, y = 320)
        headingLabel2 = tk.Label(self, image = imagen31, border = 0,bg = '#ddb892').place(x=440, y = 320)

        imagen32 = tk.PhotoImage(file ='compu.png')
        headingLabel2 = tk.Button(self, image = imagen32, border = 0,bg = '#ddb892').place(x=35, y = 235)
        headingLabel2 = tk.Button(self, image = imagen32,command=lambda: controller.show_frame(Adivin), border =0,bg = '#ddb892').place(x=470, y = 235)


        imagen33 =tk.PhotoImage(file = 'izquerda.png')
        button = tk.Button(self, image = imagen33, bg = '#cc9966', border = 0 ,command=lambda: controller.show_frame(Biblioteca))
        button.place(x = 0, y = 80)

        imagen34 =tk.PhotoImage(file = 'derecha.png')
        button = tk.Button(self, image = imagen34, bg = '#cc9966', border = 0 ,command=lambda: controller.show_frame(Servidores))
        button.place(x = 560, y = 80)

class Adivin(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg= '#E7FFFF')
        self.controller = controller
        self.controller.title('Adiv')
        self.controller.geometry('600x400')

        global user
        global clImg

        self.score = 0
        self.count = 0
        self.win_count = 0
        self.ans_str=StringVar()
        
        self.g01= api.GameInfo("Laboratorio SL001","Adivinanzas")
        self.answers = self.g01.answers
        self.question = self.g01.question
        self.clueMsg = self.g01.clueMsg

        self.question_str=StringVar()
   
        self.ckl1=clk.CountDown(self,"00","00")
        #self.ckl1.start()

        #self.lifes=[4,4,4]
        self.lifes=user.lifes
        self.lf=lifeInfo.LifeHandle(self,self.lifes)

        #self.clues=[1,1,1]
        self.clues=user.clues
        self.cl=lifeInfo.ClueHandle(self,self.clues)

        clImg=tk.PhotoImage(file="cluebtn.png")
        btnClue=tk.Button(self,bd=0,command=lambda:self.Hint(),bg="#E7FFFF",activebackground="#E7FFFF",image=clImg)
        btnClue.place(x=2,y=100)

        label_0 = tk.Label(self,text='',bg="#E7FFFF")
        label_0.pack()

        label_1 = tk.Label(self,text='',bg="#E7FFFF")
        label_1.pack()

        label_2 = tk.Label(self,text='',bg="#E7FFFF")
        label_2.pack()

        label_3 = tk.Label(self,text='',bg="#E7FFFF")
        label_3.pack()

        label_4 = tk.Label(self,text='',bg="#E7FFFF")
        label_4.pack()

        label_9 = tk.Label(self,text='',bg="#E7FFFF")
        label_9.pack()

        label_5 = tk.Label(self,text='',bg="#E7FFFF")
        label_5.pack()

        self.win = WrappingLabel(self,text=self.question,bg="#E7FFFF",font=("arial",15))
        self. win.pack(fill='x')

        label_6 = tk.Label(self,text='',bg="#E7FFFF")
        label_6.pack()

        label_7 = tk.Label(self,text='',bg="#E7FFFF")
        label_7.pack()

        entry_ans=tk.Entry(self,textvariable = self.ans_str,bg="white",font=("arial",14))
        entry_ans.pack()

        label_8 = tk.Label(self,text='',bg="#E7FFFF")
        label_8.pack()
         
        btn = tk.Button(self,text="Validate",command=self.btnClick)
        btn.pack()

        btn2 = tk.Button(self,text="Iniciar",command=lambda: self.startgame())
        btn2.pack()

        btn3 = tk.Button(self,text="Salir",command=lambda: controller.show_frame(LabSL001))
        btn3.pack()


    def btnClick(self):
        global ans_str
        global lf
        global lifes
        value=self.ans_str.get()
   
        if (value in self.answers):
            messagebox.showinfo("Answer Verification","Success Answer...")
        else:
            messagebox.showinfo("Answer Verification","Fail...")
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)

    def startgame(self):
        global user
       
        self.ckl1.minute=user.min
        self.ckl1.second=user.sec
        self.ckl1.start()

        self.lifes=user.lifes
        self.lf.updLifes(self.lifes)

        self.clues=user.clues
        self.cl.updClues(self.clues)

    def Hint(self):
        global cl
        global clueMsg
        global clues
        if (len(self.clueMsg)>0):
            messagebox.showinfo('Clue',self.clueMsg[0])
            self.cl.RemoveClue(self.clues)
            del self.clueMsg[0]


class Servidores(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg='#ddb892')
        self.controller = controller
        self.controller.title('Escape Room DD')
        self.controller.geometry('600x400')

        global imagen35
        global imagen36
        global imagen37
        global imagen38
        global imagen39
        global imagen40

     
        global user

        imagen35 = tk.PhotoImage(file ='door1.png')
        btn35 = tk.Button(self, image = imagen35,command=lambda: controller.show_frame(Rock), border = 0, bg = '#adb5bd').place(x=220, y = 130)

        imagen36 = tk.PhotoImage(file ='rank.png')
        btn36 = tk.Button(self, image = imagen36,command=lambda: controller.show_frame(Palabras), bg = '#adb5bd').place(x=15, y = 200)

        imagen37 = tk.PhotoImage(file ='papelera.png')
        btn37 = tk.Button(self, image = imagen37,command=lambda: controller.show_frame(NumAleatorio),bg = '#adb5bd').place(x=500, y = 280)

        imagen38 = tk.PhotoImage(file ='reloj.png')
        headingLabel38 = tk.Label(self, image = imagen38,bg = '#adb5bd').place(x=500, y = 50)

        headingLabel39 = tk.Label(self, text = '',border = 0, bg = '#370617').pack(fill = 'x', side = 'bottom')

        
        imagen39 =tk.PhotoImage(file = 'izquerda.png')
        button = tk.Button(self, image = imagen39, bg = '#cc9966', border = 0 ,command=lambda: controller.show_frame(Biblioteca))
        button.place(x = 0, y = 80)

        imagen40 =tk.PhotoImage(file = 'derecha.png')
        button = tk.Button(self, image = imagen40, bg = '#cc9966', border = 0 )
        button.place(x = 560, y = 80)

class Rock(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg= '#E7FFFF')
        self.controller = controller
        self.controller.title('Adiv')
        self.controller.geometry('600x400')

        global rock,paper,scissors
        
        rock = tk.PhotoImage(file='piedra.png')
        paper = tk.PhotoImage(file='papel.png')
        scissors = tk.PhotoImage(file='tijera.png')


        self.image_list = [rock, paper, scissors]


        self.pick_number = randint(0,2)


        self.image_label = tk.Label(self, image=self.image_list[self.pick_number], bd=0)
        self.image_label.pack(pady=20)


        self.user_choice = ttk.Combobox(self, value=("Rock", "Paper", "Scissors"))
        self.user_choice.current(0)
        self.user_choice.pack(pady=0)

        spin_button = tk.Button(self, text="Spin!", command=self.spin)
        spin_button.pack(pady=2)

        
        btn3 = tk.Button(self,text="Salir",command=lambda: controller.show_frame(Servidores))
        btn3.pack()

        self.win_lose_label = tk.Label(self, text="", font=("Helvetica", 12), bg="white")
        self.win_lose_label.pack(pady=10)

    def spin(self):

        self.pick_number = randint(0,2)

        self.image_label.config(image=self.image_list[self.pick_number])

	    # 0 = Rock
	    # 1 = Paper
	    # 2 = Scissors

        if self.user_choice.get() == "Rock":
            user_choice_value = 0
        elif self.user_choice.get() == "Paper":
            user_choice_value = 1
        elif self.user_choice.get() == "Scissors":
            user_choice_value = 2


        if user_choice_value == 0: # Rock
            if self.pick_number == 0:
                self.win_lose_label.config(text="It's A Tie! Spin Again...")
            elif self.pick_number == 1: # Paper
                self.win_lose_label.config(text="Paper Cover Rock! You Lose...")
            elif self.pick_number == 2: # Scissors
                self.win_lose_label.config(text="Rock Smashes Scissors!  You Win!!!")


        if user_choice_value == 1: # Paper
            if self.pick_number == 1:
                self.win_lose_label.config(text="It's A Tie! Spin Again...")
            elif self.pick_number == 0: # Rock
                self.win_lose_label.config(text="Paper Cover Rock! You Win!!!")
            elif self.pick_number == 2: # Scissors
                self.win_lose_label.config(text="Scissors Cuts Paper! You Lose...")


        if user_choice_value == 2: # Scissors
            if self.pick_number == 2:
                self.win_lose_label.config(text="It's A Tie! Spin Again...")
            elif self.pick_number == 0: # Rock
                self.win_lose_label.config(text="Rock Smashes Scissors! You Lose...")
            elif pick_number == 1: # Paper
                self.win_lose_label.config(text="Scissors Cuts Paper! You Win!!!")


class Palabras(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg= '#E7FFFF')
        self.controller = controller
        self.controller.title('Adiv')
        self.controller.geometry('600x400')

        global user

        self.score = 0
        self.count = 0
        self.win_count = 0
        self.ans_str=StringVar()
        
        self.g01= api.GameInfo("Cuarto de Servidores ","Palabra mezclada")
        self.category = self.g01.category
        self.question = self.g01.question
        self.words = self.g01.words

        self.question_str=StringVar()
   
        self.ckl1=clk.CountDown(self,"00","00")
        #self.ckl1.start()

        #self.lifes=[4,4,4]
        self.lifes=user.lifes
        self.lf=lifeInfo.LifeHandle(self,self.lifes)

        opcion = self.words[0]
        tamano = len(opcion)
        opcion1 = self.words[1]
        tamano1 = len(opcion1)
        opcion2 = self.words[2]
        tamano2 = len(opcion2)
        opcion3 = self.words[3]
        tamano3 = len(opcion3)

        desordenar = random.sample(opcion, tamano)
        palabra =''.join(desordenar)
        desordenar1 = random.sample(opcion1, tamano1)
        palabra1 =''.join(desordenar1)
        desordenar2 = random.sample(opcion2, tamano2)
        palabra2 =''.join(desordenar2)
        desordenar3 = random.sample(opcion3, tamano3)
        palabra3 =''.join(desordenar3)

        self.palabra = palabra
        self.palabra1 = palabra1
        self.palabra2 = palabra2
        self.palabra3 = palabra3
     
        label_0 = tk.Label(self,text='',bg="#E7FFFF")
        label_0.pack()

        label_1 = tk.Label(self,text='',bg="#E7FFFF")
        label_1.pack()

        label_2 = tk.Label(self,text='',bg="#E7FFFF")
        label_2.pack()

        label_3 = tk.Label(self,text='',bg="#E7FFFF")
        label_3.pack()

        label_4 = tk.Label(self,text='',bg="#E7FFFF")
        label_4.pack()

        question = WrappingLabel(self,text=self.question,bg="#E7FFFF",font=("arial",15))
        question.pack()

        label_5 = tk.Label(self,text='',bg="#E7FFFF")
        label_5.pack()

        label_category = tk.Label(self,text='Categoria: '+ self.category,bg="#E7FFFF",font=("arial",16))
        label_category.pack()

        label_palabra = tk.Label(self,text=palabra + ', ' + palabra1 + ', ' + palabra2 + ', ' + palabra3 + ', ',bg="#E7FFFF",font=("arial",16))
        label_palabra.pack()

        label_8 = tk.Label(self,text='',bg="#E7FFFF")
        label_8.pack()

        entry_ans=tk.Entry(self,textvariable = self.ans_str,bg="white",font=("arial",14))
        entry_ans.pack()

        label_8 = tk.Label(self,text='',bg="#E7FFFF")
        label_8.pack()

        btn = tk.Button(self,text="Validate",command=self.btnClick)
        btn.pack()

        
        btn2 = tk.Button(self,text="Iniciar",command=lambda: self.startgame())
        btn2.pack()

        btn3 = tk.Button(self,text="Salir",command=lambda: controller.show_frame(Servidores))
        btn3.pack()

    def btnClick(self):
        global ans_str
        global lf
        global lifes
        value=self.ans_str.get()
   
        if (value in self.words):
            messagebox.showinfo("Answer Verification","Success Answer...")
        else:
            messagebox.showinfo("Answer Verification","Fail...")
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)

    def startgame(self):
        global user
       
        self.ckl1.minute=user.min
        self.ckl1.second=user.sec
        self.ckl1.start()

        self.lifes=user.lifes
        self.lf.updLifes(self.lifes)

class NumAleatorio(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg= '#E7FFFF')
        self.controller = controller
        self.controller.title('Adiv')
        self.controller.geometry('600x400')

        global user
        global clImg



        self.score = 0
        self.count = 0
        self. win_count = 0

        
        self.g01= api.GameInfo("Cuarto de Servidores ","escoge un número entre")
        self.answer = self.g01.answer.lower()
        self.question = self.g01.question
        self.clueMsg = self.g01.clueMsg
       
   
        self.ckl1=clk.CountDown(self,"00","00")
        #self.ckl1.start()

        #self.lifes=[4,4,4]
        self.lifes=user.lifes
        self.lf=lifeInfo.LifeHandle(self,self.lifes)

        #self.clues=[1,1,1]
        self.clues=user.clues
        self.cl=lifeInfo.ClueHandle(self,self.clues)

        clImg=tk.PhotoImage(file="cluebtn.png")
        btnClue=tk.Button(self,bd=0,command=lambda:self.Hint(),bg="#E7FFFF",activebackground="#E7FFFF",image=clImg)
        btnClue.place(x=2,y=100)

        
        label_0 = tk.Label(self,text='',bg="#E7FFFF")
        label_0.pack()

        label_1 = tk.Label(self,text='',bg="#E7FFFF")
        label_1.pack()

        label_2 = tk.Label(self,text='',bg="#E7FFFF")
        label_2.pack()

        label_3 = tk.Label(self,text='',bg="#E7FFFF")
        label_3.pack()

        label_4 = tk.Label(self,text='',bg="#E7FFFF")
        label_4.pack()

        label_5 = tk.Label(self,text='',bg="#E7FFFF")
        label_5.pack()

        label_6 = tk.Label(self,text='',bg="#E7FFFF")
        label_6.pack()

        label_question = tk.Label(self,text=self.question,bg="#E7FFFF",font=("arial",18))
        label_question.pack()

        label_7 = tk.Label(self,text='',bg="#E7FFFF")
        label_7.pack()

        self.ans_str=StringVar()
        entry_ans=tk.Entry(self,textvariable = self.ans_str,bg="white",font=("arial",14))
        entry_ans.pack()

        label_8 = tk.Label(self,text='',bg="#E7FFFF")
        label_8.pack()

        btn = tk.Button(self,text="Validate",command= self.btnClick)
        btn.pack()
        self.x = random.randint(0,15)

        btn2 = tk.Button(self,text="Iniciar",command=lambda: self.startgame())
        btn2.pack()

        btn3 = tk.Button(self,text="Salir",command=lambda: controller.show_frame(Servidores))
        btn3.pack()

    def btnClick(self):
        global ans_str
        global lf
        global lifes
        value=self.ans_str.get()
   
        if (value==self.x):
            messagebox.showinfo("Answer Verification","Success Answer...")
        else:
            messagebox.showinfo("Answer Verification","Fail...")
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)
            self.lf.RemoveLife(self.lifes)

    def startgame(self):
        global user
       
        self.ckl1.minute=user.min
        self.ckl1.second=user.sec
        self.ckl1.start()

        self.lifes=user.lifes
        self.lf.updLifes(self.lifes)

    def Hint(self):
        global cl
        global clueMsg
        global clues
        if (len(self.clueMsg)>0):
            messagebox.showinfo('Clue',self.clueMsg[0])
            self.cl.RemoveClue(self.clues)
            del self.clueMsg[0]


class Saman(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self,parent, bg='#90e0ef')
        self.controller = controller
        self.controller.title('Escape Room DD')
        self.controller.geometry('600x400')


        global imagen41
        global imagen42
        global imagen43
        global imagen44
        global imagen45

        imagen41 = tk.PhotoImage(file ='arbol.png')
        headingLabel1 = tk.Button(self, image = imagen41, border = 0, bg = '#90e0ef').place(x=80, y = 80)

        imagen42 = tk.PhotoImage(file ='banco.png')
        headingLabel2a = tk.Button(self, image = imagen42,border = 0, bg = '#90e0ef').place(x=10, y = 320)
        headingLabel2b = tk.Button(self, image = imagen42, border = 0,bg = '#90e0ef').place(x=440, y = 320)

        imagen43 = tk.PhotoImage(file ='basura.png')
        headingLabel2c =tk. Label(self, image = imagen43, bg = '#90e0ef').place(x=370, y = 350)

        imagen44 = tk.PhotoImage(file ='cloud.png')
        headingLabel2d = tk.Label(self, image = imagen44, bg = '#90e0ef').place(x=50, y = 50)
        headingLabel2e = tk.Label(self, image = imagen44, bg = '#90e0ef').place(x=480, y = 120)

        imagen45 =tk.PhotoImage(file = 'derecha.png')
        button = tk.Button(self, image = imagen45,command=lambda: controller.show_frame(Biblioteca), bg = '#90e0ef', border = 0 )
        button.place(x = 560, y = 80)


defaultMin="60"
user = pt.Usuario("")
p=pt.Partida("",0)
app = EscapeRoomapp()
app.mainloop()
