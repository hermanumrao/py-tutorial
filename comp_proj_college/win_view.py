from tkinter import *
import csv

global passScreen

# Create and set the GUI for the passScreen of the Password Manager.
passScreen = Tk()
passScreen.geometry("1900x800")
passScreen.resizable(width=True, height=True)
passScreen.title("Password")

Label(passScreen, text="EventID").grid(row=3, column=1, padx=10)
Label(passScreen, text="Name").grid(row=3, column=2, padx=40)
Label(passScreen, text="Semesters participating").grid(row=3, column=3, padx=20)
Label(passScreen, text="individual/group").grid(row=3, column=4, padx=40)
Label(passScreen, text="Date&time(hr/mn/dd/mm/yyyy)").grid(row=3, column=5, padx=40)
Label(passScreen, text="1st place").grid(row=3, column=6, padx=40)
Label(passScreen, text="2nd place").grid(row=3, column=7, padx=40)
Label(passScreen, text="3rd place").grid(row=3, column=8, padx=40)
Label(passScreen, text="4th place").grid(row=3, column=9, padx=40)

passfile = open("cca_fin.csv", "r")
read = csv.reader(passfile)
data = list(read)

entrieslist = []

i = 4
for entries in list(range(0, len(data))):
    entrieslist.append(data[entries][0])

    Label(passScreen, text=data[entries][0]).grid(row=i, column=1)
    Label(passScreen, text=data[entries][1]).grid(row=i, column=2)
    Label(passScreen, text=data[entries][2]).grid(row=i, column=3)
    Label(passScreen, text=data[entries][4]).grid(row=i, column=4)
    Label(passScreen, text=data[entries][5]).grid(row=i, column=5)
    Label(passScreen, text=data[entries][6]).grid(row=i, column=6)
    Label(passScreen, text=data[entries][7]).grid(row=i, column=7)
    Label(passScreen, text=data[entries][8]).grid(row=i, column=8)
    Label(passScreen, text=data[entries][9]).grid(row=i, column=9)
    i=i+1

passScreen.mainloop()