import pickle

def fwrite():
	ans='y'
	fout=open("dict.dat",'ab')
	while ans=='y':
		rno=int(input('enter roll no. '))
		name=input("enter the name. ")
		marks=float(input('enter marks '))
		data={'roll no':rno,'name':name,'marks':marks}
		pickle.dump(data,fout)
		ans=input("do you want to continue y/n  ")
	print("data  written")
	fout.close()
def fread():
	fin=open("dict.dat",'rb')
	try:
		while True:
			st=pickle.load(fin)
			print(st)
			a=input("press any key")
	except EOFError:
			fin.close()
fwrite()
fread()