import pickle
stu={}
stufile=open('stu.dat','wb')
ans='y'
while ans == 'y':
    rn=int(input("enter the roll no. : "))
    name=input("enter the name : ")
    marks=int(input("enter the marks : "))
    stu['rollno.']=rn
    stu['Name']=name
    stu['Marks']=marks
    print(stu)
    pickle.dump(stu,stufile)
    ans=input("want more inputs : ")
stufile.close()

