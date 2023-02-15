def f3(a,b,*args,**kwargs):
	print(a,b,c,d,e)
	print(args,type(args))
	print(kwargs,type(kwargs))
f3(2,3,4,5,"abc",c='1',d='2',e='3')
