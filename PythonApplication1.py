
import tkinter as tk
from tkinter import messagebox
import json
from json import JSONEncoder
from functools import partial 
import random 
from time import sleep


LARGE_FONT= ("Verdana", 12)


class Usuario:
    def __init__(self, firstName, lastName, userName, pwd, cfm_pwd, phone):

        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.pwd = pwd
        self.cfm_pwd = cfm_pwd
        self.phone = phone

class UserEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

class WrappingLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.bind('<Configure>', lambda e: self.config(wraplength=self.winfo_width()))

class SeaofBTCapp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

 

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, Menu, StartGame, Instructions, Record, Narrativa1, Biblioteca):

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
        self.controller.title('Escape Room')
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
        userName = tk.StringVar()  
        pwd = tk.StringVar()  

        def Login(self,userName,pwd):
            #print('UserName:'+userName.get())
            #print('Pwd:'+pwd.get())
            
            #Open a File and decode 
            with open("usuario.txt", "r") as read_file:
                data = json.load(read_file)
                read_file.close

            fg_Found=False
            #Iterate List
            for user in data:
                if ((user.get('userName')==userName.get()) and (user.get('pwd')==pwd.get())):
                    fg_Found=True
                    msgBox = messagebox.askquestion('Login successful', 'Do you want to go to the main menu of the game?', icon = 'question')
                    if msgBox == 'yes':
                        self.controller.show_frame(Menu)
                    break
            if (not fg_Found):
                messagebox.showinfo('Login','Login Fail')

        

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

        button2 = tk.Button(self, text="Login", command= partial(Login,self,userName,pwd))
        button2.place(x = 200, y =300)

        def show_frame(self, cont):

            frame = self.frames[cont]
            frame.tkraise()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        global imagen4

        def Register(firstName,lastName,userName,pwd,cfm_pwd,phone):
            listUsers = []
            usuario = Usuario(firstName.get(),lastName.get(),userName.get(),pwd.get(),cfm_pwd.get(),phone.get())
            listUsers.append(usuario)
             #Open a File and decode 
            with open("usuario.txt", "r") as read_file:
                data = json.load(read_file)
                read_file.close
            
            for user in data:
                listUsers.append(user)

            jsonstr = json.dumps(listUsers, indent=2, cls=UserEncoder)
            with open('usuario.txt', 'w') as f:
                f.write(jsonstr)
                f.close


            messagebox.showinfo('Register','Register success')
       
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

        pwd_label= tk.Label(self, text = 'Password', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        pwd_label.place(x = 340, y = 160)

        pwd_entry = tk.Entry(self, textvariable = pwd, width = 29)
        pwd_entry.place(x = 360, y = 200)

        cfm_pwd_label = tk.Label(self, text = 'Confirm Password', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        cfm_pwd_label.place(x = 340, y = 240)

        cfm_pwd_entry = tk.Entry(self, textvariable = cfm_pwd,width = 29)
        cfm_pwd_entry.place(x = 360, y = 280)

        userName_label= tk.Label(self, text = 'Username', width = 20, font = ('bold',15), fg = 'white', bg = 'black')
        userName_label.place(x = 340, y = 80)

        userName_entry = tk.Entry(self, textvariable = userName, width = 29)
        userName_entry.place(x = 360, y = 120)

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

        button2 = tk.Button(self, text="Register",command=partial(Register,userName,firstName,lastName,pwd,cfm_pwd,phone))
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
        tk.Frame.__init__(self,parent, bg= 'black')
        self.controller = controller
        self.controller.title('Escape Room')
        self.controller.geometry('600x400')

        imagen11 =tk.PhotoImage(file ='select1.png')
        headingLabel1 = tk.Label(self, image = imagen11, bg = 'black').pack()

        imagen12 =tk.PhotoImage(file = 'easy1.png')
        button = tk.Button(self, image = imagen12, border = 0 , bg = 'black',command=lambda: controller.show_frame(Narrativa1))
        button.pack()
        imagen13 =tk.PhotoImage(file = 'medium1.png')
        button = tk.Button(self, image = imagen13, border = 0 , bg = 'black',command=lambda: controller.show_frame(Narrativa1))
        button.pack()
        imagen14 =tk.PhotoImage(file = 'hard1.png')
        button = tk.Button(self, image = imagen14, border = 0 , bg = 'black',command=lambda: controller.show_frame(Narrativa1))
        button.pack()


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

        tk.Frame.__init__(self,parent, bg= 'black')
        self.controller = controller
        self.controller.title('Escape Room')
        self.controller.geometry('600x400')
       

        imagen15 =tk.PhotoImage(file ='Saman_Narrativa.png')
        headingLabel1 = tk.Label(self, image = imagen15, bg = 'black').place(x=0, y=0, relwidth=1, relheight=1)

        headingaLabel_0 = WrappingLabel(self,text= 'Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad), lo que si es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda la informacion de SAP de estudiantes, pagos y asignaturas. Necesitamos que nos ayudes a recuperar el disco {tiempo_sefun_dificultad} minutos, antes de que el servidor se caiga y no se pueda hacer mas nada.',bg="black",fg= 'white',font=("arial",14))
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

        headingLabel2 = tk.Label(self, text = '' , bg = '#8c5927', width = 400)
        headingLabel2.pack(side = 'bottom', fill = 'x')

        imagen19 =tk.PhotoImage(file ='mueble.png')
        button = tk.Button(self, image = imagen19,bg = '#cc9966', border = 0,command=lambda: controller.show_frame(Narrativa1))
        button.place(x = 0, y= 260)

        imagen20 =tk.PhotoImage(file ='libros.png')
        button = tk.Button(self, image = imagen20,bg = '#cc9966', border = 0,command=lambda: controller.show_frame(Narrativa1))
        button.place(x = 200, y= 157)

        imagen21 =tk.PhotoImage(file ='mueble2.png')
        button = tk.Button(self, image = imagen21, bg = '#cc9966', border = 0,command=lambda: controller.show_frame(Narrativa1))
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
        button = tk.Button(self, image = imagen26, bg = '#cc9966', border = 0 ,command=lambda: controller.show_frame(Biblioteca))
        button.place(x = 0, y = 80)

        imagen27 =tk.PhotoImage(file = 'derecha.png')
        button = tk.Button(self, image = imagen27, bg = '#cc9966', border = 0 ,command=lambda: controller.show_frame(Biblioteca))
        button.place(x = 560, y = 80)



app = SeaofBTCapp()
app.mainloop()