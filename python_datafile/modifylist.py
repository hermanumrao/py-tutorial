import pickle 
def update():
	fin=open('list1.dat','rb+')
	st_rec=pickle.load(fin)
	found=0
	r1=int(input("enter a roll number "))
	for i in st_rec:
		if i[0]==r1:
			print("rec found",i)
			found=1
			name1=input("new name else -")
			m1=float(input('new marks else 0'))
			if name1!='-':
				i[1]=name1
			if m1!=0:
				i[2]=m1

			break
	if found==0:
		print('rec not found')
	elif found==1:
		fin.seek(0)
		pickle.dump(st_rec,fin)
		print('rec updated')
	fin.seek(0)
	l1=pickle.load(fin)
	print(l1)
update()

#2nd method
stu={}
found =False
fin=open('dict.dat','rb+')
try:
	while True:
		rpos=fin.tell()
		stu=pickle.load(fin)
		if stu['rollnu']>81:
			stu['marks']+=2
			fin.seek(rpos)
			pickle.dump(stu,fin)
			found=True

except EOFError:
	if found==False:
		print("no rec found")
	else:
		print('rec updated')
fin.seek(0)
l1=pickle.load(fin)
print(l1)
fin.close()
