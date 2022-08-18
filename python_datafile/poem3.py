fout=open("poem2.text",'a')
n=int(input())
for i in range(n):
	str1=input("enter a name ")
	fout.write(str1+' ')
	str1=input("enter roll no.  ")
	fout.write(str1+' ')

	str1=input("enter a marks ")
	fout.write(str1+'\n')
fout.close()