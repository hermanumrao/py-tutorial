a=['abc','d','ef']
print(list(map(lambda x:x.upper(),a)))
print(list(map(len,a)))
#=====================================================
n=3#int(input("enter a number"))
def f1(i):
	global n
	prod=n*i
	print(n,'x',i,'=',prod)
(map(f1,range(1,11)))