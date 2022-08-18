import pickle 
def search():
	fin=open("dict.dat",'rb')
	found=0
	try:
		while True:
			rec=pickle.load(fin)
			if rec("marks")>60 and rec("marks")<70:
				print("rec found",rec)
	except EOFError:
		fin.close()
	if found==0:
		print("rec not found")
search()