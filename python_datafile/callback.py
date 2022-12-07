def sum1(n):
	return sum(range(0,n+1))
def factorial(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return f
def operate(n,func):
	print(func(n))
n=4
if n%2==0:
	operate(n,sum1)
else:
	operate(n,factorial)

#/-------------------------------------
def msg3():
	print("hello3")
def msg2():
	print("hello2")
def msg(x):
	x()
msg3()
msg(msg3)
msg(msg2)


#/-------------------------------------
def f(*r):
	res=r[0]+r[1]+r[2]
	print(res)
def f1(*r):
	res=r[0]*r[1]*r[2]
	print(res)
def f2(func,*r):
	func(*r)
f2(f1,1,2,3,4,5,6)
f2(f,1,2,3,4,5,6)
