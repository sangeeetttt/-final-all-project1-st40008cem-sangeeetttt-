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



# LOGIN
def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("GARUDA MANAGEMENT LOGIN")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()




# LOGIN2
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="GARUDA Admin Log-In", font=('Segoe UI', 18,'bold'), width=600, bg='#1877f2',
                     fg='#ffffff')
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:", font=('Segoe UI', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:", font=('Segoe UI', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('Segoe UI', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME, font=('Segoe UI', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD, font=('Segoe UI', 25), width=15, show="*")
    password.grid(row=1, column=1)


# Button for login
    btn_login = Button(MidLoginForm, text="Login", font=('Segoe UI', 18, 'bold'), width=30,bg='#1877f2',fg='white',bd=2, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)




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
    filemenu.add_command(label="Logout")
    filemenu.add_command(label="Exit", command=Exit2)
    menubar.add_cascade(label="Account", menu=filemenu)
    Home.config(menu=menubar)
    Home.config(bg="#ffffff")

    #BUTTONS IN HOMEPAGE
    btn_addnew = Button(Title, font=('Segoe UI', 14, 'bold'), width='20', height='4', bd='2', text='Add New Product',
                        bg='#1877f2',fg='white', command=lambda: ShowAddNew())
    btn_addnew.pack(side=TOP, padx=40, pady=30, fill=X)

def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("GARUDA INVENTORY MANAGEMENT/Add new")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Product", font=('Segoe UI', 18), width=600,bg='#1877f2',fg='white')
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=50)
    lbl_productname = Label(MidAddNew, text="Product Name:", font=('Segoe UI', 25), bd=10)
    lbl_productname.grid(row=0, sticky=W)
    lbl_qty = Label(MidAddNew, text="Product Quantity:", font=('Segoe UI', 25), bd=10)
    lbl_qty.grid(row=1, sticky=W)
    lbl_price = Label(MidAddNew, text="Product Price:", font=('Segoe UI', 25), bd=10)
    lbl_price.grid(row=2, sticky=W)
    productname = Entry(MidAddNew, textvariable=PRODUCT_NAME, font=('Segoe UI', 25), width=15)
    productname.grid(row=0, column=1)
    productqty = Entry(MidAddNew, textvariable=PRODUCT_QTY, font=('Segoe UI', 25), width=15)
    productqty.grid(row=1, column=1)
    productprice = Entry(MidAddNew, textvariable=PRODUCT_PRICE, font=('Segoe UI', 25), width=15)
    productprice.grid(row=2, column=1)

    # SAVE BUTTON
    btn_add = Button(MidAddNew, text="Save", font=('Segoe UI', 18), width=30, bg="#009ACD")
    btn_add.grid(row=3, columnspan=2, pady=20)


# MENUBAR WIDGETS
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()

# LOGIN BUTTON
btn_login = Button(root, text="Click To Proceed", font=('Segoe UI', 18, 'bold'), width=30, bg="#009ACD",bd=7,fg='white', command=ShowLoginForm)
btn_login.grid(row=40, columnspan=50, pady=250, padx = 300)



# LABEL for Welcome to GARUDA
lbl_text = Label(root, text="Welcome ", font=('Open Sans', 28), bg='#e5e7e9', fg='black')
lbl_text.grid(row= 10, columnspan=50, pady=10)
lbl_text = Label(root, text="To", font=('Open Sans', 28), bg='#e5e7e9', fg='black')
lbl_text.grid(row=11, columnspan=50, pady=10)
lbl_text = Label(root, text="GARUDA INVENTORY", font=('Open Sans', 40, 'bold'), bg='#e5e7e9', fg='#1877f2')
lbl_text.grid(row= 12, columnspan=50, pady=10)

# INITIALIZATION
if __name__ == '__main__':
    root.mainloop()

