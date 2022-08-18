import pickle
def stud_write():
	record=[]
	ans='y'
	while ans=='y':
		rno=int(input('enter roll no. '))
		name=input('enter name ')
		marks=float(input('enter marks'))
		data=[rno,name,marks]
		record.append(data)
		ans=input('do you want to continue y/n  ')
	fout=open('stud1.dat','wb')
	pickle.dump(record,fout)
	print('data written')
	fout.close()

def stud_read():
	fin=open('stud1.dat','rb')
	stud_rec=pickle.load(fin)
	print(stud_rec)
	for i in stud_rec:
		r1=i[0]
		name1=i[1]
		m1=i[2]
		print(r1,name1,m1)
	fin.close()
stud_write()
stud_read()