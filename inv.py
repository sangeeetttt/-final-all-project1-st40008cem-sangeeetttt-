from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

root = Tk()
root.title("Inventory Management System by GARUDA")

width = 1024
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg='#e5e7e9')

# VARIABLES
USERNAME = StringVar()
PASSWORD = StringVar()
PRODUCT_NAME = StringVar()
PRODUCT_PRICE = IntVar()
PRODUCT_QTY = IntVar()
SEARCH = StringVar()

# EXIT
def Exit():
    result = tkMessageBox.askquestion('GARUDA Inventory Management System', 'Are you sure you want to exit?',icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Exit2():
    result = tkMessageBox.askquestion('GARUDA Inventory Management System', 'Are you sure you want to exit?',icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()




root.main()