class Sample6:
	def __init__(self):
		print("constructor called")
		print('self : ', self)
a = Sample6()
print('a : ', a)
#------------------------------------------------------------------
class mydate:
	def __init__(self,dd,mm,yy):
		self.dd=dd
		self.mm=mm
		self.yy=yy
	def int1(self):
		print("yp:")
		print(type(self.dd),self.dd)
		return self.dd+self.mm+self.yy

	def __str__(self):
		return str(self.dd)+"-"+str(self.mm)+'-'+str(self.yy)
a=mydate(2,3,4)
print('33',a.int1())
print(a)