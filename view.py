﻿import tkinter
import tkinter.font as tkFont
from tkinter import *
#from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkinter import messagebox


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class InputFrame(Frame): 
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master 
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.E4 = Entry(self)
        self.E5 = Entry(self)
        self.E6 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1


    def write(self,name,num,course,score):
        f = open('Grade.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if len(info)<4:
                break
            if info[1] ==num and info[2] ==course:
                 messagebox.showinfo(title='outcome', message ="The student's subject information already exists！")
                 f.close()
                 return

        f.close()
        f = open('Grade.csv','a',encoding='utf-8')
        f.write('{},{},{},{}\n'.format(name,num,course,score))
        f.close()
        messagebox.showinfo(title='prompt', message ="The write succeeded")
        return
    
    def click(self):
        name = self.E1.get()
        num = self.E2.get()
        course = self.E3.get()
        score = self.E4.get()
        if self.Isspace(name) or self.Isspace(num) or self.Isspace(course) or self.Isspace(score) :
            messagebox.showinfo(title='prompt', message ="The input is empty")
        else:
            self.write(name,num,course,score)
            
        
        
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)
        a = '#fafaf9'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
        self.page = Frame(self.root,bg='#fafaf9')
        self.page.pack(expand=YES,fill=BOTH)
        Label(self, text = 'name: ',font=ft,bg=a).grid(row=1, stick=W, pady=5)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text = 'Number: ',font=ft,bg=a).grid(row=2, stick=W, pady=5)
        self.E2.grid(row=2, column=1, stick=E)

        Label(self, text = 'subjects: ',font=ft,bg=a).grid(row=3, stick=W, pady=5) 
        self.E3.grid(row=3, column=1, stick=E) 

        Label(self, text = 'grades: ',font=ft,bg=a).grid(row=4, stick=W, pady=5)
        self.E4.grid(row=4, column=1, stick=E)       
        
        Button(self, text='Input',command=self.click,font=ft,bg=a).grid(row=6, column=1, stick=E, pady=10)    
class DeleteFrame(Frame):  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master 
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.createPage()
        
    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

    def delete(self,num,course):
        temp = 0
        with open("Grade.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
   
        with open("Grade.csv","w",encoding="utf-8") as f_w:
            for line in lines:
                info = line[:-1].split(",")
                if info[1] ==num and info[2] ==course:
                    temp = 1
                    continue
                f_w.write(line)
        if temp==0:
            messagebox.showinfo(title='prompt', message ="There is no such information")
        else:
            messagebox.showinfo(title='prompt', message ="The deletion is successful")
        
    def click(self):
        num = self.E1.get()
        course = self.E2.get()
        if self.Isspace(num) or self.Isspace(course):
            messagebox.showinfo(title='prompt', message ="The input is empty")
        else:
            self.delete(num,course)
            
    def createPage(self):
        a = '#fafaf9'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD) 
        self.page = Frame(self.root,bg='#fafaf9')
        Label(self).grid(row=0, stick=W, pady=10)     
        Label(self, text = 'Student ID: ',font=ft,bg=a).grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self, text = 'subjects: ',font=ft,bg=a).grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)
        Button(self, text='Delete',command=self.click,font=ft,bg=a).grid(row=6, column=1, stick=E, pady=10)   
class ModifyFrame(Frame):  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master 
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.E4 = Entry(self)
        self.E5 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

        
    def modify(self,name,num,course,score):
        temp = 0
        with open("Grade.csv","r",encoding="utf-8") as f:
            lines = f.readlines()
   
        with open("Grade.csv","w",encoding="utf-8") as f_w:
            for line in lines:
                info = line[:-1].split(",")
                if info[1] ==num and info[2] ==course:
                    temp = 1
                    f_w.write('{},{},{},{}\n'.format(name,num,course,score))
                    continue
                f_w.write(line)
        if temp==0:
            messagebox.showinfo(title='prompt', message ="There is no such information")
        else:
            messagebox.showinfo(title='prompt', message ="The modification was successful")
        
    def click(self):
        name = self.E1.get()
        num = self.E2.get()
        course = self.E3.get()
        score = self.E4.get()
        if self.Isspace(name) or self.Isspace(num) or self.Isspace(course) or self.Isspace(score) :
            messagebox.showinfo(title='prompt', message ="The input is empty")
        else:
            self.modify(name,num,course,score)   

     
    def createPage(self):  
        a = '#fafaf9'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)        
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text = 'name: ',font=ft,bg=a).grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Label(self, text = 'Student number: ',font=ft,bg=a).grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)
        Label(self, text = 'subjects: ',font=ft,bg=a).grid(row=3, stick=W, pady=10) 
        self.E3.grid(row=3, column=1, stick=E) 
        Label(self, text = 'grades: ',font=ft,bg=a).grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)    
        Button(self, text='Change',font=ft,bg=a,command=self.click).grid(row=6, column=1, stick=E, pady=10)  
class QueryFrame(Frame):  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master 
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

    def query(self,num,course):
        f = open('Grade.csv','r',encoding='utf-8')
        for line in f.readlines():
            info = line[:-1].split(",")
            if info[1] ==num and info[2] ==course:
                 messagebox.showinfo(title='outcome', message ="Name:"+info[0] +"\nStudent ID:"+info[1] +"\nsubjects:"+info[2] +"\ngrades:"+info[3] )
                 f.close()
                 return

        messagebox.showinfo(title='prompt', message ="There is no such information")
        f.close()
        return        
        
        
    def click(self):
        num = self.E1.get()
        course = self.E2.get()
        if self.Isspace(num) or self.Isspace(course):
            messagebox.showinfo(title='prompt', message ="The input is empty")
        else:
            self.query(num,course)
            
            
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        a = '#fafaf9'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)         
        Label(self, text = 'Student ID: ',font=ft,bg=a).grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text = 'subjects: ',font=ft,bg=a).grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)

        Button(self, text='Find',command=self.click,font=ft,bg=a).grid(row=6, column=1, stick=E, pady=10)  
class SortFrame(Frame): 
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master 
        self.E1 = Entry(self)
       # self.E2 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

    def sort(self,course):
        dr = pd.read_csv('Grade.csv')
        math = (dr['Subject']==course)
        ex = dr[math].sort_values(by='Grade', ascending=False)
        root = tkinter.Tk(className=" Transcripts ")
        textPad = ScrolledText(root, width=50, height=50)
        textPad.insert(tkinter.constants.END, chars = str(ex))
        textPad.pack()
        root.mainloop()
    def click(self):
        #num = self.E1.get()
        course = self.E1.get()
        if self.Isspace(course):
            messagebox.showinfo(title='prompt', message ="The input is empty")
        else:
            self.sort(course)
            
            
    def createPage(self):
        a = '#fafaf9'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text = 'subjects: ',font=ft,bg=a).grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Button(self, text='Find',command=self.click,font=ft,bg=a).grid(row=5, column=1, stick=E, pady=10) 
class AnalysisFrame(Frame):
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master
        self.E1 = Entry(self)
       # self.E2 = Entry(self)
        self.createPage()  
    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1
        
    def analyze(self, course):
        dr = pd.read_csv('Grade.csv')
        math = (dr['Subject'] == course)
        ex = dr[math].sort_values(by='Grade')
        
        # Calculate the average grade
        average_grade = ex['Grade'].mean()

        # Display pie chart
        labels = ['Good', 'Normal', 'Again']
        values = [len(ex[ex['Grade'] >= 90]), len(ex[(ex['Grade'] >= 60) & (ex['Grade'] < 90)]), len(ex[ex['Grade'] < 60])]
        colors = ['#00FA9A', '#AFEEEE', 'c']
        explode = [0, 0, 0]
        
        plt.figure(figsize=(8, 8))
        
        # Pie chart
        plt.subplot(2, 1, 1)
        plt.pie(values, labels=labels, explode=explode, colors=colors,
                startangle=180, shadow=False, autopct='%1.1f%%')
        plt.title("Grade Distribution")

        # Bar chart for average grade
        plt.subplot(2, 1, 2)
        plt.bar(['Average Grade'], [average_grade], color='orange')
        plt.title("Average Grade: {:.2f}".format(average_grade))

        plt.tight_layout()
        plt.show()

    def click(self):
        course = self.E1.get()
        if self.Isspace(course):
            messagebox.showinfo(title='prompt', message="The input is empty")
        else:
            self.analyze(course)  

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        a = '#fafaf9'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)        
        Label(self, text='subjects: ', font=ft, bg=a).grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Button(self, text='Analyze', command=self.click, font=ft, bg=a).grid(row=5, column=1, stick=E, pady=5)
    def sort(self,course):
        dr = pd.read_csv('Grade.csv')
        math = (dr['Subject']==course)
        ex = dr[math].sort_values(by='Grade')
        a = []
        good = 0
        normal = 0
        again = 0
        for devise in ex['Grade']: 
            if devise >= 90:
                good += 1
            elif (devise >= 60 and devise < 90):
                normal += 1
            else:
                again += 1
        labels = ['Good', 'Normal', 'Again']
        values = [good, normal, again]
        colors = ['#00FA9A', '#AFEEEE', 'c']
        explode = [0, 0, 0]
        plt.title("This is Grade Analysis", fontsize=25)
        plt.pie(values, labels=labels, explode=explode, colors=colors,
        startangle=180,shadow=False, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()
    def click(self):
        #num = self.E1.get()
        course = self.E1.get()
        if self.Isspace(course):
            messagebox.showinfo(title='prompt', message ="The input is empty")
        else:
            self.sort(course)  
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        a = '#fafaf9'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)        
        Label(self, text = 'subjects: ',font=ft,bg=a).grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Button(self, text='Find',command=self.click,font=ft,bg=a).grid(row=5, column=1, stick=E, pady=10) 
class CheckFrame(Frame): 
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master 
        self.E1 = Entry(self)
       # self.E2 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

    def check(self,name):
        s = pd.read_csv('Grade.csv')
        nm = (s['Name']==name)
        ex = s[nm].sort_values(by='Grade')
        root = tkinter.Tk(className=" GradeCheck！")
        textPad = ScrolledText(root, width=50, height=40)
        textPad.insert(tkinter.constants.END, chars = str(ex))
        textPad.pack()
        root.mainloop()
    def click(self):
        name = self.E1.get()
        if self.Isspace(name):
            messagebox.showinfo(title='prompt', message ="The input is empty")
        else:
            self.check(name)    
    def createPage(self):
        a = '#fafaf9'
        ft = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)  
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text = 'name: ',font=ft,bg=a).grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)
        Button(self, text='Find',command=self.click,font=ft,bg=a).grid(row=6, column=1, stick=E, pady=10)  