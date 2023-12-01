from tkinter import *
from tkinter.messagebox import *
from MainPage import *
import tkinter.font as tkFont

class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # Define the internal variable 'root'
        self.root.geometry('%dx%d' % (320, 300))  # Set window size
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        a = '#FAFAF9'
        ft = tkFont.Font(family='Helvetica', size=12, weight=tkFont.BOLD)
        self.page = Frame(self.root, bg='white')  # Create a Frame
        self.page.pack(expand=YES, fill=BOTH)
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='User: ', font=ft, bg=a).grid(row=1, stick=N, pady=5)
        Entry(self.page, textvariable=self.username, width=25).grid(row=1, column=1, stick=E)
        Label(self.page, text='Password: ', font=ft, bg=a).grid(row=2, stick=N, pady=10)
        Entry(self.page, textvariable=self.password, show='*', width=25).grid(row=2, column=1, stick=E)
        Button(self.page, text='Login', command=self.loginCheck, font=ft, bg=a).grid(row=3, column=0, pady=5)
        Button(self.page, text='SignUp', command=self.register, font=ft, bg=a).grid(row=3, column=1, pady=5)
        Button(self.page, text='Cancel', command=self.page.quit, font=ft, bg=a).grid(row=3, column=2, pady=5)

    def loginCheck(self):
        name = self.username.get()
        password = self.password.get()
        if self.isLegalUser(name, password):
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title='Error', message='Incorrect username or password!')

    def isLegal(self, string):
        alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'J', 'L', 'U', 'Z', 'H'
        ]
        for i in string:
            if i in alphabet:
                pass
            else:
                return False
        return True

    def isLegalUser(self, name, password):
        f = open('Password.csv', 'r', encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info) < 2:
                break
            if info[0].strip() == name and info[1].strip() == password:
                f.close()
                return True
        return False

    def register(self):
        name = self.username.get()
        password = self.password.get()
        if len(name) == 0 or len(password) == 0:
            showinfo(title='Error', message='Username and password cannot be empty')
            return
        for i in password:
            if i == ',' or i == ' ':
                showinfo(title='Error', message='Password cannot contain illegal characters')
                return
        if self.isLegal(name):
            pass
        else:
            showinfo(title='Error', message='Username cannot contain illegal characters')
            return
        f = open('Password.csv', 'r', encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info) < 2:
                break
            if info[0].strip() == name:
                messagebox.showinfo(title='Result', message="User information already exists!")
                f.close()
                return
        f.close()
        f = open('Password.csv', 'a', encoding='utf-8')
        f.write('{},{}\n'.format(name, password))
        f.close()
        messagebox.showinfo(title='Prompt', message="SignUp successful")