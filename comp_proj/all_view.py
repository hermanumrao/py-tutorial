from tkinter import *
import tkinter.ttk as ttk
import csv

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

with open("comp_proj/.cca_list.csv") as f:
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