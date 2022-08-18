import csv
feilds=['rno','name','marks']
'''rows=[['1','b1','45'],['2','a3','99'],['3','a3','75']]
with open('students.csv','w') as fout:
	csv_obj=csv.writer(fout)
	csv_obj.writerow(feilds)
	#csv_obj.writerows(rows)	
	for i in rows:
		csv_obj.writerow(i)
print('file created')
'''
#another method
rec=[]
while True:
	rno=int(input("enter rno"))
	name=input("enter name")
	marks=int(input("enter marks"))
	row=[rno,name,marks]
	rec.append(row)
	ans=input("do u want to enter more rows (y/n) :")
	if ans=='n':
		break
fout=open("student2.csv",'w')
csv_obj=csv.writer(fout)
csv_obj.writerow(feilds)
csv_obj.writerows(rec)
fout.close()
print("file created")
#read file
fin=open("student2.csv",'r',newline='\n')
read_obj=csv.reader(fin)
for i in read_obj:
	print(i)
fin.close()