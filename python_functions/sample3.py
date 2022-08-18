class sample3:
	def __init__(self,var1,var2):
		self.var1=var1
		self.var2=var2
	def display(self):
		print("var1=",self.var1)
		print("var2=",self.var2)

obj=sample3(10,14.5)
obj.display()
print("object.__dict__=",obj.__dict__)
print("object.__doc__=",obj.__doc__)
print("object.__name__=",sample3.__name__)
print("object.__module__=",obj.__module__)