from tkinter import *

from PIL import ImageTk, Image
def stud():
	start.destroy()
	import stud_login
def teach():
	start.destroy()
	import teach_login
start = Tk()
start.title("PES UNIVERSITY Clubs & Activities")
width = 840
height = 650
screen_width = start.winfo_screenwidth()
screen_height = start.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
start.geometry("%dx%d+%d+%d" % (width, height, x, y))
start.resizable(0, 0)
btn1 = Button(start, text="student", font=('arial', 18), width=35, command=stud)
btn1.grid(row=1, columnspan=2, pady=20)
btn1 = Button(start, text="club member", font=('arial', 18), width=35, command=teach)
btn1.grid(row=2, columnspan=2, pady=20)

image1 = ImageTk.PhotoImage(Image.open("images/01.jpg").resize((600, 350)))
image2 = ImageTk.PhotoImage(Image.open("images/02.jpg").resize((600, 350)))
image3 = ImageTk.PhotoImage(Image.open("images/03.jpg").resize((600, 350)))
image4 = ImageTk.PhotoImage(Image.open("images/04.jpg").resize((600, 350)))
image5 = ImageTk.PhotoImage(Image.open("images/05.jpg").resize((600, 350)))
image_list = [image1, image2, image3, image4, image5]
counter = 0
def ChangeImage():
    global counter
    if counter < len(image_list) - 1:
        counter += 1
    else:
        counter = 0
    imageLabel.config(image=image_list[counter])
    infoLabel.config(text="Image " + str(counter + 1) + " of " + str(len(image_list)))
imageLabel = Label(start, image=image1)
infoLabel = Label(start, text="Image 1 of 5", font="Helvetica, 20")
button = Button(start, text="Next >>", width=20, height=2, bg="purple", fg="white", command=ChangeImage)
# display the components
imageLabel.grid(row=3, columnspan=2, pady=20)
infoLabel.grid(row=3,sticky = 's')
button.grid(row=5)

if __name__ == '__main__':
    start.mainloop()
   
