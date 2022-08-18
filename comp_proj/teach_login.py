from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import csv

root = Tk()
root.title("TEACHER Login")
 
width = 840
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


#=======================================VARIABLES=====================================
USERNAME = StringVar()
PASSWORD = StringVar()
FULLNAME = StringVar()
CONFIRM_PASSWORD = StringVar()
HOUSE = StringVar()

#=======================================METHODS=======================================
def Database():
    print("database found or created")
    global conn, cursor
    conn = sqlite3.connect("db_Tmember.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `Tmember` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, fullname TEXT)")
    print("database work done")

def Admin():
    print("admin login selected")
    result = tkMessageBox.askquestion('ADMIN ONLY','Do you want to login as an admin?')
    if result == 'yes':
        print("opened admin login form")
        root.destroy()
        import admin_page


def LoginForm():
    print("login form has been open")
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    lbl_username = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)
    lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind('<Button-1>', ToggleToRegister)

def RegisterForm():
    print("registeration form has been opened")
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=40)
    lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=2)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=3)
    lbl_firstname = Label(RegisterFrame, text="Fullname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=1)
    lbl_lastname = Label(RegisterFrame, text="Confirm password:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_house = Label(RegisterFrame, text="House (R/B/Y/G):", font=('arial', 18), bd=18)
    lbl_house.grid(row=5)
    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=7, columnspan=2)
    username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=2, column=1)
    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=3, column=1)
    fullname = Entry(RegisterFrame, font=('arial', 20), textvariable=FULLNAME, width=15)
    fullname.grid(row=1, column=1)
    house = Entry(RegisterFrame, font=('arial', 20), textvariable=HOUSE, width=15)
    house.grid(row=5, column=1)
    cpassword = Entry(RegisterFrame, font=('arial', 20), textvariable=CONFIRM_PASSWORD, width=15, show="*")
    cpassword.grid(row=4, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
    btn_login.grid(row=8, columnspan=2, pady=20)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)


def ToggleToLogin(event=None):
    print("login start")
    RegisterFrame.destroy()
    LoginForm()

def ToggleToRegister(event=None):
    print("registeration start")
    LoginFrame.destroy()
    RegisterForm()

def Register():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "" or FULLNAME.get() == "" or CONFIRM_PASSWORD.get() == "" or HOUSE.get() == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    elif (CONFIRM_PASSWORD.get())!=(PASSWORD.get()):
        lbl_result2.config(text="The password and confirm password enteries don't match!", fg="orange")
    elif (HOUSE.get() not in "RBYG"):
        lbl_result2.config(text="Please enter house name R-(red) B-(bluse) G-(green) Y-(yellow)", fg="orange")
    else:
        cursor.execute("SELECT * FROM `Tmember` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `Tmember` (username, password, fullname) VALUES(?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FULLNAME.get())))
            conn.commit()
            write_file(FULLNAME.get(),USERNAME.get(),HOUSE.get())
            USERNAME.set("")
            PASSWORD.set("")
            FULLNAME.set("")
            CONFIRM_PASSWORD.set("")
            HOUSE.set("")
            print("login details saved in database")
            lbl_result2.config(text="Successfully Created!", fg="black")
        cursor.close()
        conn.close()
        print("registeration Successful")

def Login():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `Tmember` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            print("login Successful")
            LoginFrame.destroy()
            select()
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")
            print("invalid password")

def select():
    global SelectFrame
    SelectFrame = Frame(root)
    SelectFrame.pack(side=TOP, pady=40)
    btn_view = Button(SelectFrame, text="View all events ", font=('arial', 18), width=35, command=view_list)
    btn_view.grid(row=1, columnspan=2, pady=20)
    btn_view1 = Button(SelectFrame, text="View winners ", font=('arial', 18), width=35, command=view1_list)
    btn_view1.grid(row=2, columnspan=2, pady=20)

def write_file(b,c,d):
    fout=open("comp_proj/tch_list.csv",'a',newline='\n')
    fin=open("comp_proj/tch_list.csv",'r',newline='\n')
    csv_obj=csv.writer(fout)
    fin.seek(0)
    a=0
    read_obj=csv.reader(fin)
    for i in read_obj:
        a=a+1  
    rec=[a,b,c,d]
    csv_obj.writerow(rec)
    print("name added to file")
    fout.close()

def view_list():
    print("view_list")
    import all_view

def view1_list():
    print("view_list")
    import win_view
LoginForm()

#========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Admin login", command=Admin)
menubar.add_cascade(label="TEACHER ADMIN", menu=filemenu)
root.config(menu=menubar)


#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
   
