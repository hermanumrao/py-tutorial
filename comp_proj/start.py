from tkinter import *
def stud():
	start.destroy()
	import stud_login
def teach():
	start.destroy()
	import teach_login
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
   
