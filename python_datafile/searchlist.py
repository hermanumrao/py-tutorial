import pickle 
def search():
	fin=open("stud1.dat",'rb')
	rec=pickle.load(fin)
	found=0
	r1=int(input(""))
	for i in rec:
		if i[0]==r1:
			print('rec found',i)
			found=1
			break
	if found==0:
		print("rec not found")
	fin.close()
search()