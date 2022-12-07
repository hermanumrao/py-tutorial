def decorator1(func):
	def inner1():
		print("Hello, this is before function execution")
		func() # this is being decorated by decorator
		print("This is after function execution")
	return inner1
def function1(): #this is the function which is being decorated
	print("This is inside the function !!") 
def f2(): #this is the function which is being decorated
	print("enter three numbers whose avg has to be computed")
function1 =decorator1(function1) #function() getting decorated
function1 () #calls decorated function
print('-------------------------')
f2=decorator1(f2) #function() getting decorated
f2() #calls decorated function