
import tkinter as tk
from tkinter import messagebox
import json
from json import JSONEncoder

class Usuario(tk.Frame):
    def __init__(self,usr):

        self.firstName =""
        self.lastName = ""
        self.userName = ""
        self.pwd = ""
        self.cfm_pwd = ""
        self.phone = ""
        self.fg_Found=False
        self.lifes=[4,4,4,4,4]
        self.clues=[1,1,1,1,1]
        self.usr=usr
    def Login(self,controller,Menu,userName,pwd):
        #print('UserName:'+userName.get())
        #print('Pwd:'+pwd.get())
            
        #Open a File and decode 
        with open("usuario.txt", "r") as read_file:
            data = json.load(read_file)
            read_file.close


        #Iterate List
        for userInfo in data:
            if ((userInfo.get('userName')==userName.get()) and (userInfo.get('pwd')==pwd.get())):
                self.fg_Found=True
                self.firstName = userInfo.get('firstName')
                self.lastName = userInfo.get('lastName')
                self.userName = userInfo.get('userName')
                self.pwd =userInfo.get('pwd')
                self.cfm_pwd = userInfo.get('cfm_pwd')
                self.phone = userInfo.get('phone')
                msgBox = messagebox.askquestion('Login successful', 'Do you want to go to the main menu of the game?', icon = 'question')
                if msgBox == 'yes':
                    controller.show_frame(Menu)
                break
        if (not self.fg_Found):
            messagebox.showinfo('Login','Login Fail')

    def Register(self,user,firstName,lastName,userName,pwd,cfm_pwd,phone):
            self.firstName =firstName.get()
            self.lastName =lastName.get()
            self.userName =userName.get()
            self.pwd = pwd.get()
            self.cfm_pwd = cfm_pwd.get()
            self.phone = phone.get()

            listUsers = []
            
            listUsers.append(self)
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

    def NewPartida(self,level,defaultMin):
        if level==1:
            self.lifes=[4,4,4,4,4]
            self.clues=[1,1,1,1,1]
            self.min="60"
            defaultMin="60"
            self.sec="00"
        elif level==2:
            self.lifes=[4,4,4,0,0]
            self.clues=[1,1,1,0,0]
            self.min="40"
            defaultMin="40"
            self.sec="00"
        else:
            self.lifes=[4,0,0,0,0]
            self.clues=[1,1,0,0,0]
            self.min="30"
            defaultMin="30"
            self.sec="00"
    def checkUsr(self):
        if (self.usr==self.username):
            self_fg=True
       
class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

''' Child Class of Usuario Clas'''
class Partida(Usuario):
  def __init__(self, usr,ptos):
    super().__init__(usr)
    self.ptos=ptos