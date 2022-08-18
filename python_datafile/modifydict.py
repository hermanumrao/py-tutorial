#program to enter multiple student records in the form a dictionary and read the same
import pickle
import os
def stud_write():
    ans='y'
    fout=open("stud2.dat",'wb')
    while ans=='y':
        rno=int(input("Enter the Roll No."))
        name = input("Enter a name")
        marks = float(input("Enter the Marks"))
        data={"Roll No":rno, "Sname":name,"Marks":marks}
        pickle.dump(data,fout)
        ans=input("Do you want to continue - y or n")
       
    print("Data Written")
    fout.close()

def stud_read():
    fin=open("stud2.dat",'rb')
    try:
        while True:
            st_rec=pickle.load(fin)
            print(st_rec)
            
    except EOFError:
        fin.close()

def modify():
    fin=open("stud2.dat",'rb')
    fout=open("temp2.dat",'ab')
    rno=int(input("Enter roll no. to be modified"))
    found=False
    try:
        while True:
            st_rec=pickle.load(fin)
            if st_rec["Roll No"]==rno:
                print(st_rec)
                st_rec["Roll No"]=int(input("Enter the Roll No."))
                st_rec["Sname"]=input("Enter name to be modified")
                st_rec["Marks"]=float(input("Enter marks to be modified"))
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
    os.remove("stud2.dat")
    os.rename("temp2.dat","stud2.dat")

stud_write()
stud_read()
modify()
stud_read()