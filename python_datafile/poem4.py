f2=open("poem.txt","r")
f1=open("poem2.txt",'w')
str1=f2.readlines()
for i in str1:
	t=i.split()
	print(t)
	for x in t:
		f1.write(x)
		f1.write(' ')
	f1.write('\n')