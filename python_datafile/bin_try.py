import pickle
f=open("list1.dat",'wb')
record=[]
ans='y'
print('student details')
while ans=='y':
	rno=int(input("r. no. "))
f1()
fin=open("list1.dat",'rb')
a=pickle.load(fin)
print(a)
fin.close()