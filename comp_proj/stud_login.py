from tkinter import *
import sqlite3
import csv
import pickle
import os

root = Tk()
root.title("STUDENT Login")
 
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
DCLASS = StringVar()
e_id = StringVar()
#=======================================METHODS=======================================
def Database():
    print("database found or created")
    global conn, cursor
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, fullname TEXT)")


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
    lbl_class = Label(RegisterFrame, text="Class", font=('arial',18), bd=18)
    lbl_class.grid(row=6)
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
    dclass = Entry(RegisterFrame, font=('arial', 20), textvariable=DCLASS, width=15)
    dclass.grid(row=6, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
    btn_login.grid(row=8, columnspan=2, pady=20)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)

def ToggleToLogin(event=None):
    print("login complete")
    RegisterFrame.destroy()
    LoginForm()

def ToggleToRegister(event=None):
    print("registeration complete")
    LoginFrame.destroy()
    RegisterForm()

def Register():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "" or FULLNAME.get() == "" or CONFIRM_PASSWORD.get() == "" or HOUSE.get() == "" or DCLASS.get() == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    elif (CONFIRM_PASSWORD.get())!=(PASSWORD.get()):
        lbl_result2.config(text="The password and confirm password enteries don't match!", fg="orange")
    elif int(DCLASS.get()) not in range(1,13):
        lbl_result2.config(text="please enter class (1-12)", fg="orange")
    elif (HOUSE.get() not in "RBYG"):
        lbl_result2.config(text="Please enter house name R-(red) B-(bluse) G-(green) Y-(yellow)", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `member` (username, password, fullname) VALUES(?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FULLNAME.get())))
            conn.commit()
            write_file(FULLNAME.get(),USERNAME.get(),HOUSE.get(),DCLASS.get())
            USERNAME.set("")
            PASSWORD.set("")
            FULLNAME.set("")
            CONFIRM_PASSWORD.set("")
            HOUSE.set("")
            DCLASS.set("")
            print("login details saved in database")
            lbl_result2.config(text="Successfully Created!", fg="black")
        cursor.close()
        conn.close()
        print("registeration Successful")

def Login():
    Database()
    global user_name
    user_name=USERNAME.get()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            LoginFrame.destroy()
            print("login Successful")
            select()
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")
            print("invalid password")


def write_file(b,c,d,e):
    fout=open("comp_proj/stu_list.csv",'a',newline='\n')
    fin=open("comp_proj/stu_list.csv",'r',newline='\n')
    csv_obj=csv.writer(fout)
    fin.seek(0)
    a=0
    read_obj=csv.reader(fin)
    for i in read_obj:
        a=a+1  
    rec=[a,b,c,d,e]
    csv_obj.writerow(rec)
    print("name added to file")
    fout.close()

def select():
    global SelectFrame
    SelectFrame = Frame(root)
    SelectFrame.pack(side=TOP, pady=40)
    btn_view = Button(SelectFrame, text="View all events ", font=('arial', 18), width=35, command=view_list)
    btn_view.grid(row=1, columnspan=2, pady=20)
    btn_view1 = Button(SelectFrame, text="View winners ", font=('arial', 18), width=35, command=view1_list)
    btn_view1.grid(row=2, columnspan=2, pady=20)
    btn_apply = Button(SelectFrame, text="Register for event", font=('arial', 18), width=35, command=application)
    btn_apply.grid(row=3, columnspan=2, pady=20)
    #
def view_list():
    print("view_list")
    import all_view
def view1_list():
    print("view_list")
    import win_view
def application():
    SelectFrame.destroy()
    print("application")
    print("event registeration form has been opened.")
    global applyFrame, lbl_result3
    applyFrame = Frame(root)
    applyFrame.pack(side=TOP, pady=40)
    lbl_username = Label(applyFrame, text="Please enter event ID:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    username = Entry(applyFrame, font=('arial', 20), textvariable=e_id, width=15)
    username.grid(row=1, column=1)
    lbl_result3 = Label(applyFrame, text="", font=('arial', 18))
    lbl_result3.grid(row=2, columnspan=2)
    btn_login = Button(applyFrame, text="Register", font=('arial', 18), width=35, command=stud_apply)
    btn_login.grid(row=3, columnspan=2, pady=20)
    
    
def stud_apply():
    print("done")
    found=False
    fin1=open("comp_proj/.cca_list.csv",'r',newline='\n')
    print(user_name)
    read_obj1=csv.reader(fin1)
    for j in read_obj1:
        print("and")
        print(j[0],e_id.get())
        if e_id.get()==j[0]:
            print("found")
            cca_class=j[2].split(" ")
            cca_mstud=j[-3]
            found=True
    print(found)
    fin3=open("comp_proj/participant.dat",'rb')
    rno=e_id.get()
    found=False
    try:
        while True:
            st_rec=pickle.load(fin3)
            if st_rec[0]==rno:
                print(st_rec)
                mstud=len(st_rec[1])
                lstud=st_rec[1]
                found2=True
    except EOFError:
        if found2==False:
            print("Record not Found")
        else:
            print("Record found")

    fin=open("comp_proj/stu_list.csv",'r',newline='\n')
    read_obj=csv.reader(fin)
    for i in read_obj:
        if user_name==i[2]:
            stud_house=i[-2]
            stud_class=i[-1]
            print(stud_house,stud_class)
    if found2==False:
        lbl_result3.config(text="Please enter the correct event ID.", fg="orange")
    elif stud_class not in cca_class:
        lbl_result3.config(text="Your class has not been assigned this event.", fg="orange")
    elif mstud>=int(cca_mstud):
        lbl_result3.config(text="registeration for th event has been closed.", fg="orange")
    elif user_name in lstud:
        lbl_result3.config(text="you have already registered for the event.", fg="orange")
    else:
        fin4=open("comp_proj/participant.dat",'rb')
        fout4=open("temp2.dat",'ab')
        rno=e_id.get()
        found1=False
        try:
            while True:
                st_rec=pickle.load(fin4)
                if st_rec[0]==rno:
                    print(st_rec)
                    st_rec[1]=st_rec[1]+[user_name,]
                    print(st_rec)#R B G Y
                    if stud_house=='R':
                        st_rec[2]=st_rec[2]+1
                    elif stud_house=='B':
                        st_rec[3]=st_rec[3]+1
                    elif stud_house=='G':
                        st_rec[4]=st_rec[4]+1
                    elif stud_house=='Y':
                        st_rec[5]=st_rec[5]+1
                    found1=True
                    pickle.dump(st_rec,fout4)
                else:
                    pickle.dump(st_rec,fout4)
      
        except EOFError:
            if found1==False:
                print("Record not Found")
            else:
                print("Record updated")
                
            fin4.close()
            fout4.close()
        os.remove("comp_proj/participant.dat")
        os.rename("temp2.dat","comp_proj/participant.dat")

LoginForm()

#========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
   
