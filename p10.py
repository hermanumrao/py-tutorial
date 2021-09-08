a=open("security.txt","a+")
a.seek(0)
b=a.readlines()
while True:
	id1=input("enter user id   :")

	if ("user id:"+id1+'\n') in b:
		print("User Id already Exists")
	else:
		a.write("user id:"+id1+'\n')
		break
while True:
	pas=input("enter a password:")
	i=0
	if len(pas)>=8:
		i=i+1
	for j in pas:
		if j.isdigit:
			i=i+1
			break
	for j in pas:
		if j in ("$@%"):
			i=i+1
			break
	if i==3:
		a.write("password:"+pas+'\n')
		break
	else:
		print("password not valid")