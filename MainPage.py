from tkinter import *
from view import *  # Corresponding subpages for the menu bar

class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # Define the internal variable 'root'
        self.root.geometry('%dx%d' % (350, 350))  # Set window size
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)  # Create different Frames
        self.deletePage = DeleteFrame(self.root)
        self.modifyPage = ModifyFrame(self.root)
        self.queryPage = QueryFrame(self.root)
        self.sortPage = SortFrame(self.root)
        self.analysisPage = AnalysisFrame(self.root)
        self.checkPage = CheckFrame(self.root)
        self.inputPage.pack()  # Default display data entry interface

        menubar = Menu(self.root)
        menubar.add_command(label='Add Information', command=self.inputData)
        menubar.add_command(label='Delete Information', command=self.deleteData)
        menubar.add_command(label='Modify Information', command=self.modifyData)
       # menubar.add_command(label='Search by Subject', command=self.queryData)
        menubar.add_command(label='Grade Ranking', command=self.sortData)
        menubar.add_command(label='Grade Analysis', command=self.analysisData)
       # menubar.add_command(label='Search for Students', command=self.checkData)
        self.root['menu'] = menubar  # Set the menu bar

    def inputData(self):
        self.inputPage.pack()
        self.queryPage.pack_forget()
        self.deletePage.pack_forget()
        self.modifyPage.pack_forget()
        self.sortPage.pack_forget()
        self.analysisPage.pack_forget()
        self.checkPage.pack_forget()

    def deleteData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.deletePage.pack()
        self.modifyPage.pack_forget()
        self.sortPage.pack_forget()
        self.analysisPage.pack_forget()
        self.checkPage.pack_forget()

    def modifyData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.deletePage.pack_forget()
        self.modifyPage.pack()
        self.sortPage.pack_forget()
        self.analysisPage.pack_forget()
        self.checkPage.pack_forget()

    def queryData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack()
        self.deletePage.pack_forget()
        self.modifyPage.pack_forget()
        self.sortPage.pack_forget()
        self.analysisPage.pack_forget()
        self.checkPage.pack_forget()

    def sortData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.deletePage.pack_forget()
        self.modifyPage.pack_forget()
        self.sortPage.pack()
        self.analysisPage.pack_forget()
        self.checkPage.pack_forget()

    def analysisData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.deletePage.pack_forget()
        self.modifyPage.pack_forget()
        self.sortPage.pack_forget()
        self.analysisPage.pack()
        self.checkPage.pack_forget()

    def checkData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.deletePage.pack_forget()
        self.modifyPage.pack_forget()
        self.sortPage.pack_forget()
        self.analysisPage.pack_forget()
        self.checkPage.pack()
