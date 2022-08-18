from tkinter import *
import tkinter.ttk as ttk
import sqlite3
import csv
import pickle
import os
import tkinter.messagebox as tkMessageBox



#__________________________________all_view.py____________________
def all_view():
	view_all = Tk()
	view_all.title("view all events")
	width = 500
	height = 400
	screen_width = view_all.winfo_screenwidth()
	screen_height = view_all.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2)
	view_all.geometry("%dx%d+%d+%d" % (width, height, x, y))
	view_all.resizable(0, 0)


	TableMargin = Frame(view_all, width=500)
	TableMargin.pack(side=TOP)
	scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
	scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
	tree = ttk.Treeview(TableMargin, columns=("event_id","event_name","classes","max_no_stud","ind_grp","date"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
	scrollbary.config(command=tree.yview)
	scrollbary.pack(side=RIGHT, fill=Y)
	scrollbarx.config(command=tree.xview)
	scrollbarx.pack(side=BOTTOM, fill=X)
	tree.heading('event_id', text="event_id", anchor=W)
	tree.heading('event_name', text="event_name", anchor=W)
	tree.heading('classes', text="classes", anchor=W)
	tree.heading('max_no_stud', text="max_no_stud", anchor=W)
	tree.heading('ind_grp', text="ind/grp", anchor=W)
	tree.heading('date', text="date", anchor=W)
	tree.column('#0', stretch=NO, minwidth=0, width=0)
	tree.pack()

	with open("comp_proj\cca_list.csv") as f:
	    reader = csv.DictReader(f, delimiter=',')
	    for row in reader:
	        event_id = row['event_id']
	        event_name = row['event_name']
	        classes = row['classes']
	        max_no_stud = row['max_no_stud']
	        ind_grp = row['ind/grp']
	        date = row['date']
	        tree.insert("", 0, values=(event_id,event_name,classes,max_no_stud,ind_grp,date))

	#============================INITIALIZATION==============================
	if __name__ == '__main__':
	    view_all.mainloop()
#__________________________win_view.py_______________________
def win_view():
	view_all = Tk()
	view_all.title("view all events")
	width = 500
	height = 400
	screen_width = view_all.winfo_screenwidth()
	screen_height = view_all.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2)
	view_all.geometry("%dx%d+%d+%d" % (width, height, x, y))
	view_all.resizable(0, 0)


	TableMargin = Frame(view_all, width=500)
	TableMargin.pack(side=TOP)
	scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
	scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
	tree = ttk.Treeview(TableMargin, columns=("event_id","event_name","classes","max_no_stud","ind_grp","date","a1st","a2nd","a3rd","a3rd"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
	scrollbary.config(command=tree.yview)
	scrollbary.pack(side=RIGHT, fill=Y)
	scrollbarx.config(command=tree.xview)
	scrollbarx.pack(side=BOTTOM, fill=X)
	tree.heading('event_id', text="event_id", anchor=W)
	tree.heading('event_name', text="event_name", anchor=W)
	tree.heading('classes', text="classes", anchor=W)
	tree.heading('max_no_stud', text="max_no_stud", anchor=W)
	tree.heading('ind_grp', text="ind/grp", anchor=W)
	tree.heading('date', text="date", anchor=W)
	tree.heading('a1st', text="1st", anchor=W)
	tree.heading('a2nd', text="2nd", anchor=W)
	tree.heading('a3rd', text="3rd", anchor=W)
	tree.heading('a3rd', text="4th", anchor=W)

	tree.column('#0', stretch=NO, minwidth=0, width=0)
	tree.pack()

	with open("comp_proj\cca_fin.csv") as f:
	    reader = csv.DictReader(f, delimiter=',')
	    for row in reader:
	        event_id = row['event_id']
	        event_name = row['event_name']
	        classes = row['classes']
	        max_no_stud = row['max_no_stud']
	        ind_grp = row['ind/grp']
	        date = row['date']
	        a1st = row['1st']
	        a2nd = row['2nd']
	        a3rd = row['3rd']
	        a4th = row['4th']
	        tree.insert("", 0, values=(event_id,event_name,classes,max_no_stud,ind_grp,date,a1st,a2nd,a3rd,a4th))

	#============================INITIALIZATION==============================
	if __name__ == '__main__':
	    view_all.mainloop()

	   
#_______________________________________admin_page.py_____________________________-
def admin_page():

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
	
	CRTDATE = StringVar()
	CRTSTU = StringVar()
	CRTNAME = StringVar()

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
	    DELID = StringVar()
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
	    w1 = StringVar()
	    wwin = StringVar()
	    w2 = StringVar()
	    w3 = StringVar()
	    w4 = StringVar()
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
	    file=open("comp_proj\cca_list.csv",'a')
	    fin=open("comp_proj\cca_list.csv",'r')
	    fout=open("comp_proj\cca_cache.txt",'r+')
	    prticpnt=open("comp_proj\participant.dat",'ab')
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
	    fout=open("comp_proj\cca_list1.csv",'a')
	    fin=open("comp_proj\cca_list.csv",'r',newline='\n')
	    rno=str(DELID.get())
	    csv_obj=csv.writer(fout)
	    read_obj=csv.reader(fin)
	    for i in read_obj:
	        if i[0]==rno:
	            print("rec found and Deleted")
	        else:
	            print(i)
	            csv_obj.writerow(i)
	    os.remove("comp_proj\cca_list.csv")
	    os.rename("comp_proj\cca_list1.csv","comp_proj\cca_list.csv")
	    fin.close()

	def fin_file():
	    winners=[wwin.get(),w1.get(),w2.get(),w3.get(),w4.get()]
	    print(winners)
	    fin=open("comp_proj\cca_list.csv",'r',newline='\n')
	    fout=open("comp_proj\cca_fin.csv",'a')
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
	    all_view()

	def view1_list():
	    print("view_list")
	    win_view()

	LoginForm()
	if __name__ == '__main__':
	    admin.mainloop()
#_____________________________stud_login.py________________________

def stud_login():
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
	    fout=open("comp_proj\stu_list.csv",'a',newline='\n')
	    fin=open("comp_proj\stu_list.csv",'r',newline='\n')
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
	    all_view()
	def view1_list():
	    print("view_list")
	    win_view()
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
	    fin1=open("comp_proj\cca_list.csv",'r',newline='\n')
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
	    fin1.close()
               
	    print(found)
	    fin3=open("comp_proj\participant.dat",'rb')
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
	    fin3.close()

	    fin=open("comp_proj\stu_list.csv",'r',newline='\n')
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
	        fin4=open("comp_proj\participant.dat",'rb')
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
	        os.remove("comp_proj\participant.dat")
	        os.rename("temp2.dat","comp_proj\participant.dat")
	        

	LoginForm()

	#========================================INITIALIZATION===================================
	if __name__ == '__main__':
	    root.mainloop()
	   
#_________________________________teach_login.py________________________   
def teach_login():
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
	        admin_page()


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
	    fout=open("comp_proj\tch_list.csv",'a',newline='\n')
	    fin=open("comp_proj\tch_list.csv",'r',newline='\n')
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
	    all_view()

	def view1_list():
	    print("view_list")
	    win_view()
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

def stud():
	start.destroy()
	stud_login()
def teach():
	start.destroy()
	teach_login()
start = Tk()
start.title("CCA HAL Public School")
width = 840
height = 600
screen_width = start.winfo_screenwidth()
screen_height = start.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
start.geometry("%dx%d+%d+%d" % (width, height, x, y))
start.resizable(0, 0)
btn1 = Button(start, text="student", font=('arial', 18), width=35, command=stud)
btn1.grid(row=1, columnspan=2, pady=20)
btn1 = Button(start, text="teacher", font=('arial', 18), width=35, command=teach)
btn1.grid(row=2, columnspan=2, pady=20)

if __name__ == '__main__':
    start.mainloop()