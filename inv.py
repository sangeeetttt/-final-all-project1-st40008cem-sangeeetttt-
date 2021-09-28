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


# FUNCTIONS

# DATABASE
def Database():
    global conn, cursor
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, product_name TEXT, product_qty TEXT, product_price TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `sale` (p_id INTEGER, name TEXT, quantity TEXT, price_per_unit TEXT, total TEXT)")
    cursor.execute("SELECT * FROM `admin`")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()
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


def Home():
    global Home
    Home = Tk()
    Home.title("GARUDA INVENTORY MANAGEMENT/Home")
    width = 1024
    height = 720
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(Title, text="GARUDA INVENTORY MANAGEMENT", font=('Segoe UI', 35, 'underline', 'bold'))
    lbl_display.pack()

    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    menubar.add_cascade(label="Account", menu=filemenu)
    Home.config(menu=menubar)
    Home.config(bg="#ffffff")

# MENUBAR WIDGETS
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account")
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


# LOGIN BUTTON
btn_login = Button(root, text="Click To Proceed", font=('Segoe UI', 18, 'bold'), width=30, bg="#009ACD",bd=7,fg='white')
btn_login.grid(row=40, columnspan=50, pady=250, padx = 300)



# LABEL for Welcome to GARUDA
lbl_text = Label(root, text="Welcome ", font=('Open Sans', 28), bg='#e5e7e9', fg='black')
lbl_text.grid(row= 10, columnspan=50, pady=10)
lbl_text = Label(root, text="To", font=('Open Sans', 28), bg='#e5e7e9', fg='black')
lbl_text.grid(row=11, columnspan=50, pady=10)
lbl_text = Label(root, text="GARUDA INVENTORY", font=('Open Sans', 40, 'bold'), bg='#e5e7e9', fg='#1877f2')
lbl_text.grid(row= 12, columnspan=50, pady=10)


def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()



# INITIALIZATION
if __name__ == '__main__':
    root.mainloop()
