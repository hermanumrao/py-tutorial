import pickle
import os
#1-write
def fwrite():
    ans='y'
    fout=open("list1.dat",'wb')
    while ans=='y':
        rno=int(input("Enter the Roll No."))
        name = input("Enter a name")
        marks = float(input("Enter the Marks"))
        data=[rno,name,marks]
        pickle.dump(data,fout)
        ans=input("Do you want to continue - y or n")
       
    print("Data Written")
    fout.close()
#2-read
def fread():
    fin=open("list1.dat",'rb')
    try:
        while True:
            st_rec=pickle.load(fin)
            print(st_rec)
            
    except EOFError:
        fin.close()

#3-append
def fappend():
    ans='y'
    fout=open("list1.dat",'ab')
    while ans=='y':
        rno=int(input("Enter the Roll No."))
        name = input("Enter a name")
        marks = float(input("Enter the Marks"))
        data=[rno,name,marks]
        pickle.dump(data,fout)
        ans=input("Do you want to continue - y or n")
       
    print("Data Written")
    fout.close()
#4-modify
def fmodify():
    fin=open("list1.dat",'rb')
    fout=open("temp2.dat",'ab')
    rno=int(input("Enter roll no. to be modified"))
    found=False
    try:
        while True:
            st_rec=pickle.load(fin)
            if st_rec[0]==rno:
                print(st_rec)
                st_rec[0]=int(input("Enter the Roll No."))
                st_rec[1]=input("Enter name to be modified")
                st_rec[2]=float(input("Enter marks to be modified"))
                print(st_rec)
                found=True
                pickle.dump(st_rec,fout)
            else:
                pickle.dump(st_rec,fout)
  
    except EOFError:
        if found==False:
            print("Record not Found")
        else:
            print("Record updated")
            
        fin.close()
        fout.close()
    os.remove("list1.dat")
    os.rename("temp2.dat","list1.dat")
    #5-delete
def fdelete():
    fin=open("list1.dat",'rb')
    fout=open("temp2.dat",'ab')
    rno=int(input("Enter roll no. to be deleted "))
    found=False
    try:
        while True:
            st_rec=pickle.load(fin)
            if st_rec[0]!=rno:
                print(st_rec)
                found=True
                pickle.dump(st_rec,fout)
            else:
                print('rec deleted')
  
    except EOFError:
        if found==False:
            print("Record not Found")
        else:
            print("Record updated")
            
        fin.close()
        fout.close()
    os.remove("list1.dat")
    os.rename("temp2.dat","list1.dat")
#6-fsearch
def fsearch():
    fin=open("list1.dat",'rb')
    rno=int(input("Enter roll no. to be searched "))
    found=False
    try:
        while True:
            st_rec=pickle.load(fin)
            if st_rec[0]==rno:
                print(st_rec)
                found=True
    except EOFError:
        if found==False:
            print("Record not Found")
        else:
            print("Record found")
y='y'
while y=='y':
	a=int(input("ENTER YOUR CHOICE\n1-write\n2-read\n3-append\n4-modify\n5-delete\n6-search\n"))
	#1-write\n2-read\n3-append\n4-modify\n5-delete\n
	if a==1:
		fwrite()
	elif a==2:
		fread()
	elif a==3:
		fappend()
	elif a==4:
		fmodify()
	elif a==5:
		fdelete()
	elif a==6:
		fsearch()
	else:
		print("pls enter a valid input")
	y=input("do you want to continue (y/n)")