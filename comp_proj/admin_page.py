from tkinter import *
from time import sleep
import csv
import os
import pickle

admin = Tk()
admin.title("ADMIN Login")
width = 840
height = 600
screen_width = admin.winfo_screenwidth()
screen_height = admin.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

#=======================================VARIABLES=====================================
USERNAME = StringVar()
PASSWORD = StringVar()
var = StringVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
DELID = StringVar()
wwin = StringVar()
CRTDATE = StringVar()
CRTSTU = StringVar()
CRTNAME = StringVar()
w1 = StringVar()
w2 = StringVar()
w3 = StringVar()
w4 = StringVar()

def LoginForm():
    print("adminlogin form has been open")
    global Adminframe, lbl_result1
    Adminframe = Frame(admin)
    Adminframe.pack(side=TOP, pady=80)
    lbl_username = Label(Adminframe, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(Adminframe, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(Adminframe, text="", font=('arial', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(Adminframe, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(Adminframe, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(Adminframe, text="Login", font=('arial', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)

def Login():
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
        print("login not Successful")
    elif USERNAME.get == "admin" or PASSWORD.get() == "spexspex":#spexspex admin
        print("Admin login Successful")
        Adminframe.destroy()
        edit_page() 
    else:
        lbl_result1.config(text="Incorrect password or username.", fg="orange")
    
def edit_page():
    global EditFrame
    EditFrame = Frame(admin)
    EditFrame.pack(side=TOP, pady=80)
    btn_Create = Button(EditFrame, text="Create", font=('arial', 18), width=35, command=Create)
    btn_Create.grid(row=1, columnspan=2, pady=20)
    btn_Delete = Button(EditFrame, text="Delete", font=('arial', 18), width=35, command=Delete)
    btn_Delete.grid(row=2, columnspan=2, pady=20)
    btn_winner = Button(EditFrame, text="declare winner", font=('arial', 18), width=35, command=winner)
    btn_winner.grid(row=3, columnspan=2, pady=20)
    btn_view = Button(EditFrame, text="View all events ", font=('arial', 18), width=35, command=view_list)
    btn_view.grid(row=4, columnspan=2, pady=20)
    btn_view1 = Button(EditFrame, text="View winners ", font=('arial', 18), width=35, command=view1_list)
    btn_view1.grid(row=5, columnspan=2, pady=20)

def Create():
    print("Create new event has been selected")
    EditFrame.destroy()
    global CreateFrame, lbl_result1
    CreateFrame = Frame(admin)
    CreateFrame.pack(side=TOP, pady=80)
    lbl_crtname = Label(CreateFrame, text="activity name:", font=('arial', 25), bd=18)
    lbl_crtname.grid(row=1)
    lbl_crtclass = Label(CreateFrame, text="classes participating:", font=('arial', 25), bd=18)
    lbl_crtclass.grid(row=2)
    lbl_crtcnt = Label(CreateFrame, text="max number of students:", font=('arial', 25), bd=18)
    lbl_crtcnt.grid(row=4)
    lbl_crtwin = Label(CreateFrame, text="individual/group:", font=('arial', 25), bd=18)
    lbl_crtwin.grid(row=5)
    lbl_crtdate = Label(CreateFrame, text="activity date (format: hh/mm/dd/mm/yy):", font=('arial', 25), bd=18)
    lbl_crtdate.grid(row=6)

    crtname = Entry(CreateFrame, font=('arial', 20), textvariable=CRTNAME, width=15)
    crtname.grid(row=1, column=1) 
    c1 = Checkbutton(CreateFrame, text='1',variable=var1, onvalue=1, offvalue=0)
    c1.grid(row=2,column=1)
    c2 = Checkbutton(CreateFrame, text='2',variable=var2, onvalue=1, offvalue=0)
    c2.grid(row=2,column=2)
    c3 = Checkbutton(CreateFrame, text='3',variable=var3, onvalue=1, offvalue=0)
    c3.grid(row=2,column=3)
    c4 = Checkbutton(CreateFrame, text='4',variable=var4, onvalue=1, offvalue=0)
    c4.grid(row=2,column=4)
    c5 = Checkbutton(CreateFrame, text='5',variable=var5, onvalue=1, offvalue=0)
    c5.grid(row=2,column=5)
    c6 = Checkbutton(CreateFrame, text='6',variable=var6, onvalue=1, offvalue=0)
    c6.grid(row=2,column=6)
    c7 = Checkbutton(CreateFrame, text='7',variable=var7, onvalue=1, offvalue=0)
    c7.grid(row=3,column=1)
    c8 = Checkbutton(CreateFrame, text='8',variable=var8, onvalue=1, offvalue=0)
    c8.grid(row=3,column=2)
    c9 = Checkbutton(CreateFrame, text='9',variable=var9, onvalue=1, offvalue=0)
    c9.grid(row=3,column=3)
    c10 = Checkbutton(CreateFrame, text='10',variable=var10, onvalue=1, offvalue=0)
    c10.grid(row=3,column=4)
    c11 = Checkbutton(CreateFrame, text='11',variable=var11, onvalue=1, offvalue=0)
    c11.grid(row=3,column=5)
    c12 = Checkbutton(CreateFrame, text='12',variable=var12, onvalue=1, offvalue=0)
    c12.grid(row=3,column=6)
    crtdate = Entry(CreateFrame, font=('arial', 20), textvariable=CRTDATE, width=15)
    crtdate.grid(row=6, column=1)
    R1 = Radiobutton(CreateFrame, text="individual", variable=var, value="individual")
    R1.grid(row=5,column=2)
    R2 = Radiobutton(CreateFrame, text="group", variable=var, value="group")
    R2.grid(row=5,column=3)
    crtmaxstu = Entry(CreateFrame, font=('arial', 20), textvariable=CRTSTU, width=15)
    crtmaxstu.grid(row=4, column=1)
    lbl_result1 = Label(CreateFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=7, columnspan=2)  
    btn_submit = Button(CreateFrame, text="Submit", font=('arial', 18), width=35, command=crt_submit)
    btn_submit.grid(row=8, columnspan=2, pady=20)

def Delete():
    global lbl_del1,DELID
    DeleteFrame= Frame(admin)
    DeleteFrame.pack(side=TOP, pady=80)
    print("Delete existing event  has been selected")
    EditFrame.destroy()
    lbl_delid = Label(DeleteFrame, text="enter event ID:", font=('arial', 25), bd=18)
    lbl_delid.grid(row=1)
    delname = Entry(DeleteFrame, font=('arial', 20), textvariable=DELID, width=15)
    delname.grid(row=1, column=1)
    btn_del = Button(DeleteFrame, text="Delete event", font=('arial', 18), width=35, command=del_file)
    btn_del.grid(row=8, columnspan=2, pady=20)
    lbl_del1 = Label(DeleteFrame, text="", font=('arial', 25), bd=18)
    lbl_del1.grid(row=3, columnspan=2)

def winner():
    global wwin,w1,w2,w3,w4
    EditFrame.destroy()
    WinFrame= Frame(admin)
    WinFrame.pack(side=TOP, pady=80)
    print("declare winner is selected")
    lbl_win = Label(WinFrame, text="event ID", font=('arial', 25), bd=18)
    lbl_win.grid(row=1)
    lbl_1st = Label(WinFrame, text="1st place", font=('arial', 25), bd=18)
    lbl_1st.grid(row=2)
    lbl_2nd = Label(WinFrame, text="2nd place", font=('arial', 25), bd=18)
    lbl_2nd.grid(row=3)
    lbl_3rd = Label(WinFrame, text="3rd place", font=('arial', 25), bd=18)
    lbl_3rd.grid(row=4)
    lbl_4th = Label(WinFrame, text="4th place", font=('arial', 25), bd=18)
    lbl_4th.grid(row=5)
    l_win = Entry(WinFrame, font=('arial', 20), textvariable=wwin, width=15)
    l_win.grid(row=1, column=1)
    l_1 = Entry(WinFrame, font=('arial', 20), textvariable=w1, width=15)
    l_1.grid(row=2, column=1)
    l_2 = Entry(WinFrame, font=('arial', 20), textvariable=w2, width=15)
    l_2.grid(row=3, column=1)
    l_3 = Entry(WinFrame, font=('arial', 20), textvariable=w3, width=15)
    l_3.grid(row=4, column=1)
    l_4 = Entry(WinFrame, font=('arial', 20), textvariable=w4, width=15)
    l_4.grid(row=5, column=1)
    btn_win = Button(WinFrame, text="done", font=('arial', 18), width=35, command=fin_file)
    btn_win.grid(row=6, columnspan=2, pady=20)

def crt_submit():
    class_list=""
    if var1.get() == 1:
        class_list=class_list+" "+"1"
    if var2.get() == 1:
        class_list=class_list+" "+"2"
    if var3.get() == 1:
        class_list=class_list+" "+"3"
    if var4.get() == 1:
        class_list=class_list+" "+"4"
    if var5.get() == 1:
        class_list=class_list+" "+"5"
    if var6.get() == 1:
        class_list=class_list+" "+"6"
    if var7.get() == 1:
        class_list=class_list+" "+"7"
    if var8.get() == 1:
        class_list=class_list+" "+"8"
    if var9.get() == 1:
        class_list=class_list+" "+"9"
    if var10.get() == 1:
        class_list=class_list+" "+"10"
    if var11.get() == 1:
        class_list=class_list+" "+"11"
    if var12.get() == 1:
        class_list=class_list+" "+"12"
    print("classes",class_list)
    date=CRTDATE.get().split('/')
    print(date)
    tdate=False
    for i in date:
        if i.isdigit and len(i)<3:
            tdate=True
        else:
            tdate=False
    if CRTNAME.get == "" or CRTSTU.get() == "" or CRTDATE.get() == "" or var.get() == "" or class_list== "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    elif CRTSTU.get().isdigit()!=True:
        lbl_result1.config(text="max number of students must be an integer", fg="orange")
    elif len(date)!=5 or tdate==False:
        lbl_result1.config(text="Please enter date in correct format", fg="orange")
    else:
        print("creation Successful")
        write_file(CRTNAME.get(),class_list,CRTSTU.get(),var.get(),CRTDATE.get())

def write_file(b,c,d,e,f):
    file=open("comp_proj/.cca_list.csv",'a')
    fin=open("comp_proj/.cca_list.csv",'r')
    fout=open("comp_proj/.cca_cache.txt",'r+')
    prticpnt=open("comp_proj/participant.dat",'ab')
    fin.seek(0)
    fout.seek(0)
    read_obj=fout.readline().split()
    a=""
    for i in read_obj:
        a=str(int(read_obj[-1])+1)
    fout.write(a+' ')
    rec=[a,b,c,d,e,f]
    csv_obj=csv.writer(file)
    csv_obj.writerow(rec)
    data1=[a,[],0,0,0,0]
    pickle.dump(data1,prticpnt)
    print("new event has been created")
    file.close()
    fin.close()
    fout.close()
    prticpnt.close()

def del_file():
    fout=open("comp_proj/.cca_list1.csv",'a')
    fin=open("comp_proj/.cca_list.csv",'r',newline='\n')
    rno=str(DELID.get())
    csv_obj=csv.writer(fout)
    read_obj=csv.reader(fin)
    for i in read_obj:
        if i[0]==rno:
            print("rec found and Deleted")
        else:
            print(i)
            csv_obj.writerow(i)
    os.remove("comp_proj/.cca_list.csv")
    os.rename("comp_proj/.cca_list1.csv","comp_proj/.cca_list.csv")

def fin_file():
    winners=[wwin.get(),w1.get(),w2.get(),w3.get(),w4.get()]
    print(winners)
    fin=open("comp_proj/.cca_list.csv",'r',newline='\n')
    fout=open("comp_proj/cca_fin.csv",'a')
    csv_obj=csv.writer(fout)
    read_obj=csv.reader(fin)
    for i in read_obj:
        print(i,winners)
        if i[0]==winners[0]:
            print("rec found and updated")
            csv_obj.writerow(i+winners[1::])
        else:
            print("_")
    fin.close()
    fout.close()

def view_list():
    print("view_list")
    import all_view

def view1_list():
    print("view_list")
    import win_view

LoginForm()
if __name__ == '__main__':
    admin.mainloop()
   