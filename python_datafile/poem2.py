f2=open("poem.txt","r")
import string
asd=string.punctuation
vou='aeiouAEIOU'
con='bcdfghijklmnpqrstvwxyzBCDFGHJKLMNPQRSTUVWXYZ'
str1=f2.readlines()
s=0
for i in str1:
	for j in i:
		if j.isupper():
			s=s+1
print('no. of upper case ',s)
s=0
for i in str1:
	for j in i:
		if j.isdigit():
			s=s+1
print('no. of digits ',s)
s=0
for i in str1:
	for j in i:
		if j in asd:
			s=s+1
print('no. of special charecters ',s)
s=0
for i in str1:
	for j in i:
		if j in con:
			s=s+1
print('no. of consonants ',s)
s=0
for i in str1:
	for j in i:
		if j in vou:
			s=s+1
print('no. of vouvels ',s)
s=0
for i in str1:
	l=i.split()
	for 'leaf' in l:
		s=s+1
print('no. of leaf ',s)